gcc -c -Wall -Werror -fpic client.cpp
#gcc -c -o client.o client.cpp
gcc -shared -o libClient.so client.o


#ar rcs Client.a client.o  for static library
