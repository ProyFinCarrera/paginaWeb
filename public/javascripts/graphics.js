    const btnNum1 = document.getElementById("btnNum1");
    const btnNum2 = document.getElementById("btnNum2");
    const btnNum3 = document.getElementById("btnNum3");
    const btnNum4 = document.getElementById("btnNum4");

    const inputSeachUser = document.getElementById("inputSeachUser");
    const inputSelect = document.getElementById("inputSelect");

    const firestore = firebase.firestore();
    const settings = { timestampsInSnapshots: true };
    firestore.settings(settings);

    // Load the Visualization API and the piechart package.
    google.charts.load('current', { 'packages': ['corechart', 'table'] });
    btnNum1.addEventListener('click', () => {
        // Set a callback to run when the Google Visualization API is loaded.
        google.charts.setOnLoadCallback(draw1());
    });

    btnNum2.addEventListener('click', () => {
        // Set a callback to run when the Google Visualization API is loaded.
        google.charts.setOnLoadCallback(draw2());
    });

    btnNum3.addEventListener('click', () => {
        // Set a callback to run when the Google Visualization API is loaded.
        google.charts.setOnLoadCallback(draw3());
    });

    btnNum4.addEventListener('click', () => {
        // Set a callback to run when the Google Visualization API is loaded.
        google.charts.setOnLoadCallback(draw4());
    });

    function contPersonYearDay(year, month, day,name_day) {
        return new Promise(function(resolve, reject) {
            var mac = inputSelect.value
            let db = null
            if (mac == "ALL") {
                db = firestore.collection('passVerification').where('year', '==', year).where('month', '==', month).where('day', '==', day).get()
            } else {
                db = firestore.collection('passVerification').where('year', '==', year).where('month', '==', month).where('day', '==', day).where('mac', '==', mac).get();
            }
            let cont = 0;
            db.then(function(querySnapshot) {
                var array = new Array()
                querySnapshot.forEach(function(doc) {
                    cont += 1
                });
                array.push(name_day)
                array.push(cont)
                resolve(array);
            }).catch(function(error) {
                reject(error);
            });
        })
    }

    function selecDevice() {
        db = firestore.collection('device').get()
        db.then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                let opt = document.createElement("option");
                opt.setAttribute("value", doc.data().mac);
                opt.innerHTML = doc.data().name + "//" + doc.data().mac
                inputSelect.appendChild(opt);
            });


        }).catch(function(error) {
            reject(error);
        });

    }
    window.onload = selecDevice();

    function contPersonYear(year, month, day_week) {
        return new Promise(function(resolve, reject) {
            var data = new Array();
            new_day = day_week
            new_day = 24
            for (var i = 0; i < 7; i++) {
                contPersonYearDay(year, month, new_day,dayWeek[i]).then(function(doc) {
                    data.push(doc);
                    if (data.length == 7) {
                        resolve(data);
                    }
                })
                new_day += 1
            }
        }).catch(function(error) {
            reject(error);
        });

    }

    var dayWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

    function draw2() {
        clearDiv();
        let today = new Date();
        let thisMonth = today.getMonth() + 1;
        let thisYear = today.getFullYear();
        let start_week = start_day_week(today) //today.getFullYear();
        // console.log(start_week)
        contPersonYear(thisYear, thisMonth, start_week).then(function(arrayCont) {
            if (!arrayCont.empty) {
                // Create the data table.
                var data = new google.visualization.DataTable();
                // Create a query against the collection
                // console.log(arrayCont)
                data.addColumn('string', 'Day');
                data.addColumn('number', 'Count');
                data.addRows(arrayCont);
                let sum = sumArrayArray(arrayCont);
                var options = { 'title': 'Number of people identified each day of this week. Total Register: ' + sum };
                // Instantiate and draw our chart, passing in some options.
                var chart = new google.visualization.PieChart(document.getElementById('graphics'));
                chart.draw(data, options);
            }
        });
    }

    function sumArrayArray(array) {
        let suma = 0;
        for (let i = 0; i < array.length; i++) {
            suma += array[i][1];
        }
        return suma;
    }

    function start_day_week(date) {
        day = date.getDay();
        if (day == 0) {
            day = (-6);
        } else {
            day = (day - 1)
        }
        return (date.getDate() - day)
    }
    /*devuelvo persona con y hora*/
    function searchWorkPosition(emailId) {
        return new Promise(function(resolve, reject) {
            let db = firestore.collection('users').where('emailId', '==', emailId).get()
            db.onSnapshot(function(querySnapshot) {
                var work;
                querySnapshot.forEach(function(doc) {
                    work = doc.data().workPosition;
                });
                resolve(work)
            }).catch(function(error) {
                reject(error);
            });
        })
    }

    function clearDiv() {
        let myNode = document.getElementById("graphics");
        while (myNode.firstChild) {
            myNode.removeChild(myNode.firstChild);
        }
        myNode = null
    }

    function draw1() {
        clearDiv();
        let today = new Date();
        let thisDay = today.getDate();
        let thisMonth = today.getMonth() + 1;
        let thisYear = today.getFullYear();
        // console.log(thisDay)
        var array = [];
        // 12 / 3/2019
        personAccessToday(thisDay, thisMonth, thisYear).then(function(users) {
            // Create the data table.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name');
            data.addColumn('string', 'email');
            //data.addColumn('string', 'Work-Position');
            /*var i;
            workPositionArray(users).then(function(dato) {
                var ar = new Array(dato)

                console.log(ar["0"][1])

                for (i = 0; i < users.length; i++) {
                                        
                 // users[i][2] = dato[0][i];
                  // console.log(dato.pop())
                }
            })*/
            data.addColumn('string', 'Device');
            data.addColumn('string', 'Hour');
            data.addRows(users);
            var table = new google.visualization.Table(document.getElementById('graphics'));
            table.draw(data, { showRowNumber: true, width: '100%' });



        })

    }
    /*devuelvo persona con y hora*/
    function workPositionArray(array) {
        return new Promise(function(resolve, reject) {
            var i
            var list = []
            for (i = 0; i < array.length; i++) {
                workPosition(array[i][1]).then(function(work) {

                    list.push(work)
                    //list = list + work
                    //console.log(work)

                })
                resolve(list)
            }



        })
    }

    function workPosition(email) {
        return new Promise(function(resolve, reject) {
            db = firestore.collection('users').where('emailId', '==', email).get();

            db.then(function(querySnapshot) {
                var array = new Array();
                querySnapshot.forEach(function(doc) {
                    // array.push(doc.data().workPosition );
                    resolve(doc.data().workPosition)
                })
                //resolve(array)

            })

        })
    }

    /*devuelvo persona con y hora*/
    function personAccessToday(day, month, year,) {
        return new Promise(function(resolve, reject) {
            var mac = inputSelect.value
            let db = null
            if (mac == "ALL") {
                db = firestore.collection('passVerification').where('day', '==', day).where('month', '==', month).where('year', '==', year).get();
            } else {
                db = firestore.collection('passVerification').where('day', '==', day).where('month', '==', month).where('year', '==', year).where('mac', '==', mac).get();
            }

            db.then(function(querySnapshot) {
                var array = [];
                querySnapshot.forEach(function(doc) {
                    var auxArray = new Array()
                    min = ('0' + doc.data().minute).slice(-2);
                    hour = ('0' + doc.data().hour).slice(-2);
                    hourFull = hour + ":" + min;
                    // searchWorkPosition(doc.data().emailId).then(function(work) {
                    //     auxArray.push(doc.data().firstName);
                    //     auxArray.push(work);
                    //     auxArray.push(hourFull);
                    //     array.push(auxArray);
                    //     console.log(doc.data())   
                    //     if(cont ==50){
                    //       resolve(array);    
                    //     }
                    // })
                    auxArray.push(doc.data().firstName);
                    auxArray.push(doc.data().emailId);
                    // auxArray.push("");
                    auxArray.push(doc.data().mac);
                    auxArray.push(hourFull);
                    array.push(auxArray)
                    resolve(array);
                });

            })
        })
    }

    function getWeekInMonth(year, month, day) {
        let weekNum = 1; // we start at week 1 
        let weekDay = new Date(year, month - 1, 1).getDay(); // we get the weekDay of day 1 
        weekDay = weekDay === 0 ? 6 : weekDay - 1; // we recalculate the weekDay (Mon:0, Tue:1, Wed:2, Thu:3, Fri:4, Sat:5, Sun:6) 
        let monday = 1 + (7 - weekDay); // we get the first monday of the month 
        while (monday <= day) { //we calculate in wich week is our day 
            weekNum++;
            monday += 7;
        }
        return weekNum; //we return it
    }

    function weeksOfThisMonth(year, month) {
        return new Promise(function(resolve, reject) {

            var mac = inputSelect.value
            let db = null
            if (mac == "ALL") {
                db = firestore.collection('passVerification').where('month', '==', month).where('year', '==', year).get();
            } else {
                db = firestore.collection('passVerification').where('month', '==', month).where('year', '==', year).where('mac', '==', mac).get();
            }
            let week1 = 0;
            let week2 = 0;
            let week3 = 0;
            let week4 = 0;
            let week5 = 0;
            db.then(function(querySnapshot) {
                var month = Array()
                querySnapshot.forEach(function(doc) {
                    //console.log(doc);
                    var week = getWeekInMonth(doc.data().year, doc.data().month, doc.data().day);
                    switch (week) {
                        case 1:
                            week1 += 1;
                            break;
                        case 2:
                            week2 += 1;
                            break;
                        case 3:
                            week3 += 1;
                            break;
                        case 4:
                            week4 += 1;
                            break;
                        case 5:
                            week5 += 1;
                            break;
                        default:
                            console.log("Erro no found week of this month");
                            break;
                    }
                });
                month.push(week1);
                month.push(week2);
                month.push(week3);
                month.push(week4);
                month.push(week5);
                resolve(month)
            }).catch(function(error) {
                reject(error);
            });
        })
    }

    function draw3() {
        // Create the data table.jsapii
        //console.log(getWeekInMonth(2019, 3, 10));
        // this month Dicenbes is 11, add +1
        clearDiv();
        let thisMonth = new Date().getMonth() + 1;
        let thisYear = new Date().getFullYear();
        // console.log(thisMonth);
        weeksOfThisMonth(thisYear, thisMonth).then(function(contWeek) {
            var data = null
            if (contWeek.length == 5) {
                data = google.visualization.arrayToDataTable([
                    ["Element", "Density", { role: "style" }],
                    ["Week 1", contWeek[0], "#f6f461"],
                    ["Week 2", contWeek[1], "#db3d3d"],
                    ["Week 3", contWeek[2], "#b87333"],
                    ["Week 4", contWeek[3], "color: #65cf7a"],
                    ["Week 5", contWeek[4], "color: #5961bf"]
                ]);
            } else {
                data = google.visualization.arrayToDataTable([
                    ["Element", "Density", { role: "style" }],
                    ["Week 1", contWeek[0], "#f6f461"],
                    ["Week 2", contWeek[1], "#db3d3d"],
                    ["Week 3", contWeek[2], "#b87333"],
                    ["Week 4", contWeek[3], "color: #65cf7a"]
                ]);
            }
            var view = new google.visualization.DataView(data);
            view.setColumns([0, 1,
                {
                    calc: "stringify",
                    sourceColumn: 1,
                    type: "string",
                    role: "annotation"
                },
                2
            ]);
            let sum = sumArray(contWeek)

            var options = {
                title: "People for each week of this month. Total Register: " + sum,
                bar: { groupWidth: "95%" },
                legend: { position: "none" },
                width: '100%',
                height: '100%'
            };
            //let aux = document.getElementById('graphics')
            //console.log(aux.clientWidth)
            //console.log(aux.clientHeight)
            //aux.style.height = "350px";
            //aux.clientHeight = 350
            var chart = new google.visualization.ColumnChart(document.getElementById('graphics'));
            chart.draw(view, options);
        });
    }

    function sumArray(array) {
        let suma = 0;
        for (let i = 0; i < array.length; i++) {
            suma += array[i];
        }
        return suma;
    }



    function getSeachUser(name) {
        return new Promise(function(resolve, reject) {
            var mac = inputSelect.value
            let db = null
            if (mac == "ALL") {
                db = firestore.collection('passVerification').where('firstName', '==', name).get();
            } else {
                db = firestore.collection('passVerification').where('firstName', '==', name).where('mac', '==', mac).get();
            }
            let cont = 0;
            db.then(function(querySnapshot) {
                var array = new Array()
                querySnapshot.forEach(function(doc) {
                    var auxArray = new Array();

                    auxArray.push(doc.data().firstName);
                    auxArray.push(doc.data().emailId);
                    auxArray.push(doc.data().mac);

                    let day = doc.data().day;
                    let month = doc.data().month;
                    let year = doc.data().year;
                    let date = day + "/" + month + "/" + year;
                    auxArray.push(date);

                    let min = ('0' + doc.data().minute).slice(-2);
                    let hour = ('0' + doc.data().hour).slice(-2);
                    let hourFull = hour + ":" + min;
                    auxArray.push(hourFull);
                    array.push(auxArray);
                });
                // console.log(array)
                resolve(array)
            })
        })
    }

    function draw4() {
        clearDiv();
        // etiqueta nombre
        name = inputSeachUser.value;
        //nameUno
        getSeachUser(name).then(function(users) {
            // Create the data table.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name');
            data.addColumn('string', 'Email');
            data.addColumn('string', 'Device');
            data.addColumn('string', 'Date of pass');
            data.addColumn('string', 'Hour');

            data.addRows(users);
            data.sort({ column: 3, desc: true });
            var table = new google.visualization.Table(document.getElementById('graphics'));
            table.draw(data, { showRowNumber: true, width: '90%' });
        })
    }
