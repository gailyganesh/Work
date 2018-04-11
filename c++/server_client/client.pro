# Set the version of this library
VERSION = 0.1.0

HEADERS += inc/server.h
SOURCES +=src/client/client.cpp
# where to place the stuff?
DESTDIR   = bin


# additional include paths
INCLUDEPATH += src/client
INCLUDEPATH += inc

# we are building a library here
TEMPLATE = app

CONFIG += QT

TARGET      = Client

