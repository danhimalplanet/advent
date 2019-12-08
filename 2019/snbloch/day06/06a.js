var _ = require('lodash');
var tree_util = require('tree-util');

var orbits = [{'id': 'COM'}];
var depths = new Set();
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

function depth (node) {
    if (!node.parentid) {
        return 0;
    }
    else {
        return 1 + depth(node.parent);
    }
}

function calculate (node) {
    if (node.children.length) {
        depths.add({'nodeId': node.id, 'depth': depth(node)});
        node.children.forEach(function (i) {
            calculate(i);
        });
    }
    else {
        depths.add({'nodeId': node.id, 'depth': depth(node)});
    }
    return node;
}

function main() {
    buildOrbits();
    calculate(orbits[0].rootNode);
    var totalOrbits = 0;
    depths.forEach(function (i) {
        totalOrbits += i.depth;
    });
    console.log(totalOrbits);
}

main();