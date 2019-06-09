    const btnNum1 = document.getElementById("btnNum1");
    const btnNum2 = document.getElementById("btnNum2");
    const btnNum3 = document.getElementById("btnNum3");
    const btnNum4 = document.getElementById("btnNum4");

    const inputSeachUser = document.getElementById("inputSeachUser");

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
    
    function contPersonYearDay(year, name_day) {
        return new Promise(function(resolve, reject) {
            let db = firestore.collection('passVerification').where('nameDay', '==', name_day).where('year', '==', year).get()
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

    function contPersonYear(year) {
        return new Promise(function(resolve, reject) {
            var data = new Array();
            for (var i = 0; i < 7; i++) {
                contPersonYearDay(year, dayWeek[i]).then(function(doc) {
                    data.push(doc);
                    if (data.length == 7) {
                        resolve(data);

                    }
                })

            }
        }).catch(function(error) {
            reject(error);
        });

    }

    var dayWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    function draw2() {
        clearDiv();
        let thisMonth = new Date().getMonth() + 1;
        contPersonYear(2019).then(function(arrayCont) {
            if (!arrayCont.empty) {
                // Create the data table.
                var data = new google.visualization.DataTable();
                // Create a query against the collection
                // console.log(arrayCont)
                data.addColumn('string', 'Day');
                data.addColumn('number', 'Count');
                data.addRows(arrayCont);
                var options = { 'title': 'How many people for day and year' };
                // Instantiate and draw our chart, passing in some options.
                var chart = new google.visualization.PieChart(document.getElementById('graphics'));
                chart.draw(data, options);
            }
        });
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
    }
    function draw1() {
        clearDiv();
        let today = new Date();
        let thisDay = today.getDate();
        let thisMonth = today.getMonth() + 1;
        let thisYear = today.getFullYear();
        console.log(thisDay)
        var array = [];
        // 12 / 3/2019
        personAccessToday(thisDay , thisMonth,thisYear).then(function(users) {
            // Create the data table.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name');
            data.addColumn('string', 'Work-Position');
            data.addColumn('string', 'Date');
            data.addRows(users);
            var table = new google.visualization.Table(document.getElementById('graphics'));
            table.draw(data, { showRowNumber: true, width: '100%' });             
        })

    }
    /*devuelvo persona con y hora*/
    function personAccessToday(day, month, year) {
        return new Promise(function(resolve, reject) {
            let db = firestore.collection('passVerification').where('day', '==', day).where('month', '==', month).where('year', '==', year);
            db.onSnapshot(function(querySnapshot) {
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

    function weeksOfThisMonth(month) {
        return new Promise(function(resolve, reject) {
            let db = firestore.collection('passVerification').where('month', '==', month).get();
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
        // console.log(thisMonth);
        weeksOfThisMonth(thisMonth).then(function(contWeek) {
            // console.log(contWeek[1]);
            var data = google.visualization.arrayToDataTable([
                ["Element", "Density", { role: "style" }],
                ["Week 1", contWeek[1], "#f6f461"],
                ["Week 2", contWeek[2], "#db3d3d"],
                ["Week 3", contWeek[3], "#b87333"],
                ["Week 4", contWeek[4], "color: #65cf7a"],
                ["Week 5", contWeek[5], "color: #5961bf"]
            ]);

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

            var options = {
                title: "People for each week of this month",
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

    function getSeachUser(name) {
        return new Promise(function(resolve, reject) {

            let db = firestore.collection('passVerification').where('firstName', '==', name)
            let cont = 0;
            db.onSnapshot(function(querySnapshot) {
                var array = new Array()
                querySnapshot.forEach(function(doc) {
                    var auxArray = new Array();

                    auxArray.push(doc.data().firstName);
                    auxArray.push(doc.data().emailId);

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
            data.addColumn('string', 'Date of pass');
            data.addColumn('string', 'Hour');
            data.addRows(users);
            var table = new google.visualization.Table(document.getElementById('graphics'));
            table.draw(data, { showRowNumber: true, width: '90%' });
        })
    }
