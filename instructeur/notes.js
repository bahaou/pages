function js_function_that_gets_string() {
    var string = 'baha';
    return string
}

function generate() {  
    var doc = new jsPDF('p', 'pt', 'letter');  
    var group = $("#group").text();
    var ins = $("#ins").text();
    var matiere = $("#matiere").text();
    var htmlstring = '';  
    var tempVarToCheckPageHeight = 0;  
    var pageHeight = 0;  
    pageHeight = doc.internal.pageSize.height;  
    specialElementHandlers = {  
        // element with id of "bypass" - jQuery style selector  
        '#bypassme': function(element, renderer) {  
            // true = "handled elsewhere, bypass text extraction"  
            return true  
        }  
    };  
    margins = {  
        top: 150,  
        bottom: 60,  
        left: 40,  
        right: 40,  
        width: 600  
    };  
    var y = 20;  
    doc.setLineWidth(2);  
    doc.text(220, y = y + 30, "Notes du groupe "+group);  
    doc.text(250, y=y+30, matiere);  
    doc.text(20, 20, ins)
    doc.autoTable({  
        html: '#simple_table',  
        startY: y+30,  
        theme: 'grid',  
        columnStyles: {  
            0: {  
                cellWidth: 100,  
            },  
            1: {  
                cellWidth: 0,  
            },  
            2: {  
                cellWidth: 50,  
            },  
            3: {  
                cellWidth: 60,  
            },  
            4: {  
                cellWidth: 60,  
            },  
            5: {  
                cellWidth: 60,  
            },  
            
            
            
            
        },  
        styles: {  
            CellHeight: 20  
        }  
    })  
    doc.save('notes_groupe'+group+'_'+matiere+'.pdf');  
}  
