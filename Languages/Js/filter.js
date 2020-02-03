const _ = {};

_.filter = function(arr, cb) {
    //create a new array
    const storage = [];
    //loop through through arr

    _.each(arr, function(item, i, list) {
        if (cb(item, i, list) === true) {
            storage.push(item);
        }
    })


    // for (let i = 0; i < arr.length; i++) {
    //     if (cb(arr[i], i, arr) === true) { //check if cb return true
    //         storage.push(arr[i]) //if returns true,push into array
    //     }
    // }

    //return arr
    return storage;
}