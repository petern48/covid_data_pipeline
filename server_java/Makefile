all: target/server_java-1.0-SNAPSHOT.jar

target/server_java-1.0-SNAPSHOT.jar: src/main/java/server_java/*.java
	mvn package

clean:
	mvn clean

run:
	export CLASSPATH=target/server_java-1.0-SNAPSHOT.jar
	mvn exec:java -Dexec.mainClass="server_java.App"

	# java -cp target/server_java-1.0-SNAPSHOT.jar server_java.App

test:
	mvn test