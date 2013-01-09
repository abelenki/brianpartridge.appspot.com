# brianpartridge.appspot.com

## Description

The source for any of my little utils running on Google AppEngine.

## Usage

- Open GoogleAppEngineLauncher.
- Add a new Application and point it to this directory.
- Test locally then Deploy.

## Features

### WWDC -> Pingdom

Implemented in monitor.py.

Checks the WWDC conference page for changes in content and returns an XML response in Pingdom format.  If the desired string isn't found on the page, a BAD result will be returned.  Have Pingdom monitor this script to be notified when the WWDC page changes.

## License

MIT - See LICENSE.txt

## Contact

Brian Partridge - @brianpartridge on Twitter and alpha.app.net