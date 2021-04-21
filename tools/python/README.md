# AppLink via python

Python scripts to communicate with Wizzilab's AppLink

- watch_reports.py allows to display reports coming from sensors
- read_example.py allows to read a property of a device 
- write_example.py allows to configure a property of a device 

## Installation

In order to use these scripts you just need to install the paho-mqtt module

```
pip3 install paho-mqtt
```

## Tools

Once this is done, it is possible to run the scripts. The -h option is available to get a list of the required parameters.

### Watch reports

The watch_reports.py script requires the login credentials that can be found on the Dash7Board the company's page in the AppLink section. For example to connect to the queue with the following login credentials  

| MQTT Host             | roger.wizzilab.com  |
| --------------------- | ------------------- |
| Port                  | 8883                |
| User                  | xfj2l79tn5f2        |
| Client ids            | xfj2l79tn5f2:[0-9]  | 
| MQTT Topics           | /applink/01BC50C7/# | 
| Key                   | password            |

just run the following command: 

```
./watch_reports.py -b roger.wizzilab.com -p 8883 -c 01BC50C7 -u xfj2l79tn5f2 -pass password -id 0
```

### Read a property

The read_example script, which reads a property from the sensor, requires three additional parameters. The uid of the device, the file id of the file containing the searched parameter and finally the name of the desired field. A description of the available properties and their associated file ids is available in XML format at https://dash7board.wizzilab.com/devices/UID/host_xml. Here is an extract from the file https://dash7board.wizzilab.com/devices/001BC50C7001087A/host_xml
```xml
<file file_id="131" forward="2" name="Sensors Report">
        .
        .
        .
    <s16 name="temperature" display_name="Ambiant Temperature" access="r">
        <description>Ambiant Temperature Level in 10th Degree Celcius.</description>
        <actions>
            <readwritefield />
        </actions>
        <profile chart_id='temperature_chart' color='990ab2' label='Tamb'/>
    </s16>

</file>
```
For example, to obtain the temperature of the sensor with id 001BC50C7001087A, we can run this command:

```
./read_example.py -b roger.wizzilab.com -p 8883 -c 01BC50C7 -u xfj2l79tn5f2 -pass password -id 0 -uid 001BC50C7001087A -fid 131 -field temperature
```
### Write a property

To write a property, we simply add the val parameter which corresponds to the numerical value we wish to set. The script is limited to number-typed fields, so tags of type u8, u16, u32, s8, s16 and s32 are supported. Here is an example of a supported tag 
```xml
<u16 name="obs_period_s" display_name="On-Board Sensors Reporting Period" access="rw">
    <description>Onboard Sensors Refresh Period (in seconds)</description>
    <actions>
        <readwritefield/>
    </actions>
</u16>
```
To change the reporting frequency of sensor 001BC50C7001087A, we can use the following command: 

```
./write_example.py -b roger.wizzilab.com -p 8883 -c 01BC50C7 -u xfj2l79tn5f2 -pass password -id 0 -uid 001BC50C7001087A -fid 129 -field obs_period_s -val 35
```
