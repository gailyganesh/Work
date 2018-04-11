#include"server.h"
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include<string.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#define PORTNO 7960
#define SERVER_ID "127.0.0.1"
void error(const char *msg)
{
    perror(msg);
    exit(1);
}
int iport=PORTNO;
char server_id[128]="127.0.0.1";
void validatecommandline(int argc, char *argv[])
{
    for(int i=0;i<argc;i++)
    {
        if(argv[i][1]=='p')
          iport=atoi(&argv[i][3]);
        else if (argv[i][1]=='s')
          strcpy(server_id,&argv[i][3]);
    }
}
void value_to_object(iae* gaily)
{
    gaily->clas=102;
    strcpy(gaily->student.name,"ganesh");
    gaily->student.no=9688869474;
}


int main(int argc, char *argv[])
{
     int sockfd, newsockfd,clilen,n;
     char buffer[256];
     struct sockaddr_in serv_addr, cli_addr;
     // create a socket
     // socket(int domain, int type, int protocol)
     sockfd =  socket(AF_INET, SOCK_STREAM, 0);
     if (sockfd < 0)
        error("ERROR opening socket");


    //validate the command line
    validatecommandline(argc,argv);
    iae gaily;
    value_to_object(&gaily);

     /* setup the host_addr structure for use in bind call */
     // server byte order
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = inet_addr(server_id);

     // convert short integer value for port must be converted into network byte order
     serv_addr.sin_port = htons(iport);

     // bind(int fd, struct sockaddr *local_addr, socklen_t addr_length)
     // bind() passes file descriptor, the address structure,
     // and the length of the address structure
     // This bind() call will bind  the socket to the current IP address on port, portno
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0)
              error("ERROR on binding");

     // This listen() call tells the socket to listen to the incoming connections.
     // The listen() function places all incoming connection into a backlog queue
     // until accept() call accepts the connection.
     // Here, we set the maximum size for the backlog queue to 5.
     listen(sockfd,5);

     // The accept() call actually accepts an incoming connection
     clilen = sizeof(cli_addr);

     // This accept() function will write the connecting client's address info
     // into the the address structure and the size of that structure is clilen.
     // The accept() returns a new socket file descriptor for the accepted connection.
     // So, the original socket file descriptor can continue to be used
     // for accepting new connections while the new socker file descriptor is used for
     // communicating with the connected client.
     newsockfd = accept(sockfd,
                 (struct sockaddr *) &cli_addr,(socklen_t *) &clilen);
     if (newsockfd < 0)
          error("ERROR on accept");

     printf("server: got connection from %s port %d\n",
            inet_ntoa(cli_addr.sin_addr), ntohs(cli_addr.sin_port));


     // This send() function sends the 13 bytes of the string to the new socket
     for(;;)
     {
     send(newsockfd,(const void*) &gaily, sizeof(gaily), 0);
       }
//     bzero(buffer,256);

//     n = read(newsockfd,buffer,255);
//     if (n < 0) error("ERROR reading from socket");
//     printf("Here is the message: %s\n",buffer);

     close(newsockfd);
     close(sockfd);
     return 0;
}
