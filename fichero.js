var fs = require('fs');
var path = require('path');
console.log(__dirname)
let path_dir_tmp = __dirname
path_dir_tmp = path.join(path_dir_tmp, "public")
path_dir_tmp = path.join(path_dir_tmp, "video")
path_dir_tmp = path.join(path_dir_tmp, "images")
console.log(path_dir_tmp)
let path_dir_save = __dirname
path_dir_save = path.join(path_dir_save, "bin")
path_dir_save = path.join(path_dir_save, "recognizerVideo")
path_dir_save = path.join(path_dir_save, "recognizer")
path_dir_save = path.join(path_dir_save, "att_faces")
path_dir_save = path.join(path_dir_save, "orl_faces")
console.log(path_dir_save)

move("Estoy aki",path_dir_tmp, path_dir_save, function(err) {
    console.log(err)
})

function move(name, dir_oldPath, newPath, callback) {
    newPath = path.join(newPath, name)
    if (!fs.existsSync(newPath)) {
        fs.mkdirSync(newPath);//fs.mkdirSync(newPath, 0744);
    }
    }
    console.log(dir_oldPath)
    console.log(newPath)
    fs.readdir(dir_oldPath, (err, files) => {
        if (err) throw err;

        for (const file of files) {
            fs.rename(path.join(dir_oldPath, file), path.join(newPath, file), function(err) {
                if (err) {
                    if (err.code === 'EXDEV') {
                        copy();
                    } else {
                        callback(err);
                    }
                    return;
                }
                callback("Archivo move");
            });

        }
    });


    function copy() {
        var readStream = fs.createReadStream(oldPath);
        var writeStream = fs.createWriteStream(newPath);

        readStream.on('error', callback);
        writeStream.on('error', callback);

        readStream.on('close', function() {
              fs.unlink(oldPath, callback); // delete todo.
        });

        readStream.pipe(writeStream);
    }
}