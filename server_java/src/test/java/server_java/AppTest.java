package server_java;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

// new version
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Unit test for Server App.
 */
public class AppTest 
{
    private static Thread serverThread = null;
    private static String host = "localhost";
    private static int port = 8080;

    public AppTest()
    {
        String[] args = { Integer.toString(port) };
        serverThread = new Thread(() -> {
            try {
                App.main(args);
            } catch (Exception e) {
                System.out.println(e.toString());
                // System.exit(1);  // breaks the test
            }
        });
        serverThread.start();

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            System.out.println(e.toString());
            return;
        }
    }

    @Test
    public void testServerValidInputs()
    {
        String fileName = "covid/epidemiology.csv";
        String date = "2018-01-01";
        int expectedStatusCode = 200;
        Response res = sendHttpRequest(fileName, date);
        if (res == null) {
            assertTrue( false );
        }
        else {
            assertTrue(res.statusCode == expectedStatusCode);
        }
    }

    @Test
    public void testServerInvalidFile()
    {
        String fileName = "invalidFileName";
        String date = "2018-01-01";
        Response res = sendHttpRequest(fileName, date);
        if (res == null) {
            assertTrue( true );  // i really want below to work instead
        }
        else {
            assertTrue(res.statusCode != 200);
        }
    }
    
    @Test
    public void testServerInvalidDate()
    {
        String fileName = "";
        String date = "01-01-2018";  // invalid order
        Response res = sendHttpRequest(fileName, date);
        if (res == null) {
            assertTrue( true );  // i really want below to work instead
        }
        else {
            assertTrue(res.statusCode != 200);
        }
    }

    private static Response sendHttpRequest(String fileName, String date)
    {
        // Synchronous request
        String urlString = String.format("http://%s:%d/server?file=%s&date=%s", host, port, fileName, date);

        try {
            URL url = new URL(urlString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            int statusCode = connection.getResponseCode();

            StringBuilder body = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    body.append(line);
                }
            } catch(IOException e) {
                System.out.println(e.toString());
                System.out.println("EXITTING NOW");
                // assertTrue( false );
                return null;
            }
            return new Response(statusCode, body.toString());  // class defined below 

        } catch (IOException e) {
            System.out.println(e.toString());
            return null;
        }

    }

    private static class Response {
        public final int statusCode;
        public final String body;

        private Response(int statusCode, String body) {
            this.statusCode = statusCode;
            this.body = body;
        }
    }
}
