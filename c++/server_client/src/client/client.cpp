#include"server.h"
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include<string.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#define SERVER_PORT 7960
#define SERVER_ID "127.0.0.1"
#define DEFAULT_BUFFER 204800

void error(const char *msg)
{
    perror(msg);
    exit(1);
}
int iport=SERVER_PORT;
char server_id[128]=SERVER_ID;
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
int main(int argc, char *argv[])
{

    validatecommandline(argc,argv);
    char* szBuffer = new char[DEFAULT_BUFFER];  // allocate on heap
    int sclient,ret;

    struct sockaddr_in server;
    sclient = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if ( sclient == -1 )
       {
           error("socket not created properly");
           return 1;
       }
    server.sin_family      = AF_INET;
    server.sin_port        = htons(iport);
    server.sin_addr.s_addr = inet_addr(server_id);
    if (connect( sclient, (struct sockaddr *)&server, sizeof( server ) ) == -1 )
            {
                error("Connection Problem");
                sleep( 1 );
            }
    fprintf( stderr, "connected!\n" );

    unsigned int  bytesInBuffer = 0;
    size_t        bufferSize    = sizeof( iae );
    unsigned char *pData        = ( unsigned char* ) calloc( 1, bufferSize );

    for(int i=0;i<10;i++)
    {
        ret = recv( sclient, szBuffer, DEFAULT_BUFFER, 0 );
        if ( ret == -1 )
        {
           error( "recv() failed" );
            break;
        }
        if(ret!=0)
        {
            if ( ( bytesInBuffer + ret ) > bufferSize )
            {
                pData      = ( unsigned char* ) realloc( pData, bytesInBuffer + ret );
                bufferSize = bytesInBuffer + ret;
            }
            memcpy( pData + bytesInBuffer, szBuffer, ret );
            bytesInBuffer += ret;
            iae* gaily1=(iae*)pData;
            std::cout<<gaily1->student.name<<std::endl<<gaily1->student.no<<std::endl<<gaily1->clas<<std::endl;
        }
    }

    close(sclient);
    return 0;

}
