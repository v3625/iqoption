#!/bin/sh

mc admin user add my user1 testtest
mc admin policy set my readwrite user=user1

mc mb my/test
mc cp /root/testimage.jpg my/test/

