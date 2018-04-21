#include "pysensor.h"
#include "ui_pysensor.h"

PySensor::PySensor(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::PySensor)
{
    ui->setupUi(this);
}

PySensor::~PySensor()
{
    delete ui;
}
