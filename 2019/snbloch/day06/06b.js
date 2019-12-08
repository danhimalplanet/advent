var _ = require('lodash');
var tree_util = require('tree-util');
var pathFromYOU = [];
var pathFromSAN = [];

var orbits = [{'id': 'COM'}];
var standardConfig = {id: 'id', parentid: 'parentid'};
var inputfile = 'input.txt';

function buildOrbits () {
    require('fs').readFileSync(inputfile, 'utf-8').split(/\r?\n/).forEach(function(line){
        var nodeName = line.split(')')[1];
        var parent = line.split(')')[0];
        orbits.push({'id': nodeName, 'parentid': parent});
    });
    orbits = tree_util.buildTrees(orbits, standardConfig);
}

function main() {
    buildOrbits();
    startingLocation = orbits[0].getNodeById('YOU');
    currentLocation = startingLocation;
    while (currentLocation.parentid) {
        pathFromYOU.push(currentLocation.parentid);
        currentLocation = currentLocation.parent;
    }
    startingLocation = orbits[0].getNodeById('SAN');
    currentLocation = startingLocation;
    while (currentLocation.parentid) {
        pathFromSAN.push(currentLocation.parentid);
        currentLocation = currentLocation.parent;
    }
    pivot = _.intersection(pathFromYOU, pathFromSAN)[0];
    console.log(pathFromYOU.indexOf(pivot) + pathFromSAN.indexOf(pivot));
}

main();