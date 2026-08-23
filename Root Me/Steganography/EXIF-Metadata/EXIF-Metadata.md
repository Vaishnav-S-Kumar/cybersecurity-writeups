# EXIF - Metadata

## Description

Our sad friend pepo got lost! Can you find where he is ?

The password is the city where pepo is located.

## Solution

Download the challenge file using ```wget```;

```
wget <link>
```
The challenge file is an image. To find the city location, use the metadata of the image. 

Metadata is data (or information) that defines and describes the characteristics of other data. It often helps to describe, explain, locate, or otherwise make data easier to retrieve, use, or manage. For example, date, time, location and so on. 

To find metadata, use the tool exiftool which prints the metadata of the file.
```
exiftool <filename>
```
To find the specific data related to the location, use the following command;
```
exiftool <filename> | grep GPS
```
Using the GPS position data, find the city name. Use the following website; 
```
https://www.gps-coordinates.net/
```
Use the city name for password to finish the challenge.
