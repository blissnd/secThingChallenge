# secThingChallenge

Usage
======
To follow an existing /var/log/apache2/access.log =>
  > python script.py follow
  
To process an existing /var/log/apache2/access.log =>
  > python script.py batch
  
Log must be in the format (via LogFormat lines ending in %D) given in the sample apache2.conf

A sample access.log is included

[Scripts were developed & run on my localhost WordPress install]
