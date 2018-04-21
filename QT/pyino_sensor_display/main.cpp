#include "pysensor.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    PySensor w;
    w.show();

    return a.exec();
}
