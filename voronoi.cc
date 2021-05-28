#include "voro++.hh"
using namespace voro;

double rnd() {return double(rand())/RAND_MAX;}

int main() {
  double x,y,z,rsq,r;
  voronoicell v;

  v.init(0,1,0,1,0,1);

  for(int i=0;i<250;i++)  {
    x=rnd();
    y=rnd();
    z=rnd();
    v.plane(x,y,z,1);
  }

  v.draw_gnuplot(0,0,0,"voronoi.gnu");
}
