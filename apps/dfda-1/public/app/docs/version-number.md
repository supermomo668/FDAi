### How to Update the Version Number
The third digit (patch version number) in the version number is auto-generated by the gulp task and is always set to the current day of the month. 

Each month, the second digit should be manually increased by 0.1 in IONIC_IOS_APP_VERSION_NUMBER in `gulpfile.js` in root of repository. Commit version update to Github.