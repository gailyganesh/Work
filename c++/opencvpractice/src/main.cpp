#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main( )
{

       Mat image;

       image=imread("/home/gailyganesh/work/c++/opencvpractice/image1.jpg",IMREAD_COLOR);
       //cout<<image;
       namedWindow("Wild",WINDOW_AUTOSIZE);
       imshow("Wild", image);
       waitKey(0);

}
