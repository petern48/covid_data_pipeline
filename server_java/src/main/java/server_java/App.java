package server_java;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.core.ResponseBytes;

// import com.amazonaws.AmazonServiceException;


import io.github.cdimascio.dotenv.Dotenv;
import io.github.cdimascio.dotenv.DotenvEntry;

public class App 
{

    private final static String dataDir = "../data";

    private static Dotenv dotenv = Dotenv.configure().directory("..").load();

    private static Region region = Region.US_WEST_1;

    private static String bucketName = dotenv.get("S3_BUCKET");
    private static S3Client s3 = S3Client.builder().region(region).build();


    public static void main(String[] args) throws IOException {
        int port = 8080;
        if (args.length > 0) {
            port = Integer.parseInt(args[0]);
        }
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/server", new ClientHandler());  // request handler
        server.setExecutor(null);
        server.start();

        System.out.println("Server started on port " + port);
    }

    static class ClientHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if ("GET".equals(exchange.getRequestMethod())) {
                Map<String, String> params = parseQueryString(exchange.getRequestURI().getQuery());
                String fileName = params.get("file");
                String date = params.get("date");

                if (fileName == null || date == null) {
                    sendResponse(exchange, 400, "Missing file or datetime parameter");
                    return;
                }

                try {
                    LocalDate.parse(date, DateTimeFormatter.ofPattern("yyyy-MM-dd"));  // ISO_LOCAL_DATE
                } catch (Exception e) {
                    System.out.println(e.getMessage());
                    sendResponse(exchange, 400, "Invalid datetime format. Use ISO_LOCAL_DATE");
                    return;
                }

                // System.out.println("Working Directory = " + System.getProperty("user.dir"));

                String keyName = fileName;  // "covid/epidemiology.csv";
                System.out.println("keyName: " + keyName);
                String content = "";
                try {
                    GetObjectRequest objReq = GetObjectRequest.builder().key(keyName).bucket(bucketName).build();
    
                    ResponseBytes<GetObjectResponse> objectBytes = s3.getObjectAsBytes(objReq);
                    
                    byte[] contentBytes = objectBytes.asByteArray();
                    
                    // contentBytes = Arrays.copyOfRange(contentBytes, 0, 20);
                    
                    System.out.println("Successfully obtained bytes from an S3 object");
                    // exchange.getResponseHeaders().set("Content-Type", "text/css")
                    sendResponse(exchange, 200, contentBytes);


                    // Path filePath = Paths.get(dataDir, "example.csv");
                    // if (!Files.exists(filePath)) {
                    //     sendResponse(exchange, 404, "File not found");
                    //     return;
                    // }
                    // content = new String(Files.readAllBytes(filePath), StandardCharsets.UTF_8);
                    // sendResponse(exchange, 200, content);

                } catch (IOException e) {
                    e.printStackTrace();
                    sendResponse(exchange, 500, "IOException");
                } catch (S3Exception e) {
                    System.err.println(e.awsErrorDetails().errorMessage());
                    sendResponse(exchange, 404, "S3Exception: File not found");
                }
            } else {
                sendResponse(exchange, 405, "Method Not Allowed");
            }
        }

        private Map<String, String> parseQueryString(String query) throws UnsupportedEncodingException {
            Map<String, String> result = new HashMap<>();
            if (query != null) {
                for (String param : query.split("&")) {
                    String[] pair = param.split("=");
                    if (pair.length > 1) {
                        result.put(URLDecoder.decode(pair[0], "UTF-8"), URLDecoder.decode(pair[1], "UTF-8"));
                    } else {
                        result.put(URLDecoder.decode(pair[0], "UTF-8"), "");
                    }
                }
            }
            return result;
        }

        private void sendResponse(HttpExchange exchange, int statusCode, String response) throws IOException {
            exchange.sendResponseHeaders(statusCode, response.length());
            try (OutputStream os = exchange.getResponseBody()) {
                os.write(response.getBytes());
            }
        }

        private void sendResponse(HttpExchange exchange, int statusCode, byte[] response) throws IOException {
            exchange.sendResponseHeaders(statusCode, response.length);
            try (OutputStream os = exchange.getResponseBody()) {
                os.write(response);
            }
        }
    }
}
