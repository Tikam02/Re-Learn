const _ = {};

_.map = function(list, callback) {
    //create an empty array to store
    var storage = [];
    //loopin 
    for (var i = 0; i < list.length; i++) {
        //callback(element)
        //push it to our array
        storage.push(callback(list[i], i, list))
    }
    return storage;
    //return []
}

_.map([1, 2, 3], function(val) { return val + 1; })
    //=>[2,3,4]