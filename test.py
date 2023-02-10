base = '''
<!DOCTYPE html>
    <head>
        <style>
            @media print {
                .teacher {page-break-after: always;}
            }
            
            @page {
                size: 21cm 29.7cm;
                margin: 7mm 10mm 7mm 12mm;
                .teacher {page-break-after: always;}
            }
            /* #print {
                height: 29.7cm;
            } */
            #print > .container:not(:first-child) {
                margin-top: 0em;
            }
            *{
                padding: 0;
                margin: 0;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }
            body {
                width: 21cm;
            }
            p {
                font-size: .9em;
            }
            .container {
                display : grid;
                grid-template-rows: .5fr .5fr 2fr 2fr;
                line-height: .1em;
                position: relative;
                height: 29.7cm;
            }
            
            .heading {
                display: grid;
                grid-template-columns: .45fr 3fr;
                line-height: 2.3em;
            }
            .heading_title {
                display: grid;
                line-height: 1.6em;
                padding-left: .3em;
            }
            .f {
                font-weight: bold;
            }
            .title_right {
                position: absolute;
                margin-top: 3em;
                margin-left: 44em;
                font-size: .70em;
                /* border: 1px solid red; */
                display: grid;
                justify-content: right;
            }
            .title_right_container {
                /* height: 17em; */
                line-height: .9em;
                width: 23em;
                /* border: 1px solid red; */
                display: grid;
                grid-template-columns: 1.5fr .8fr .8fr;
                border-left: .5px solid black;
                border-top: .5px solid black;
                border-bottom: .5px solid black;
                font-size: 1.1em;
            }
            .title_right_container > span:nth-child(1) {
                border-bottom: .5px solid black;
            }
            .title_right_container > span:nth-child(2) {
                border-bottom: .5px solid black;
                padding-left: 0px !important;
                text-align: center;
            }
            .title_right_container > span:nth-child(3) {
                border-bottom: .5px solid black;
                padding-left: 0px !important;
                text-align: center;
            }
            .title_right_container > span {
                border-right: .5px solid black;
                padding-left: .3em;
                padding: .1em;
            }
            .title_right_container > span:nth-child(3n+2) {
                padding-left: 40%;
            }
            .title_right_container > span:nth-child(3n+3) {
                padding-left: 35%;
            }
            .heading_logo {
                display: grid;
                align-items: center;
                justify-content: center;
            }
            .logo {
                /* padding-left: 2em; */
                height: 4.9em;
                /* width: 5em; */
            }
            
            .info {
                width: 60%;
                display: grid;
                font-size: .85em;
                grid-template-columns: 2fr .2fr 4.5fr;
                line-height: 1.5em;
            }
            .table {
                font-size: 0.8em;
                display: grid;
                line-height: 1.1em;
                grid-template-columns: .5fr 2fr .3fr .5fr .5fr;
            }
            /* .table > span {
                border: 1px solid black;
            } */
            .table > span:nth-child(-n + 4) {
                border-bottom: 1px solid black;
                padding-bottom: .2em;
                font-weight: bold;
                text-align: center;
            }
            .table > span:nth-child(-n + 3) {
                display: grid;
                align-items: center;
                justify-content: center;
            }
            .table > span {
                /* padding-top: .3em; */
                padding: .15em 0em .15em .2em;
                text-align: center;
                border-left: .5px solid black;
                border-bottom: .5px solid black;
            }
            .table > span:nth-child(4) {
                grid-column: 4/6;
            }
            .table > span:nth-child(5n + 4) {
                text-align: center;
                border-right: .5px solid black;
            }
            .table > span:nth-child(1) {
                border-top: .5px solid black;
            }
            .table > span:nth-child(2) {
                border-top: .5px solid black;
            }
            .table > span:nth-child(3) {
                border-top: .5px solid black;
            }
            .table > span:nth-child(4) {
                border-top: .5px solid black;
            }
            .double_row {
                display: grid;
                grid-template-columns: 1fr 1fr;
            }
            .double_row > span:nth-child(1) {
                grid-column: 1/3;
                border-bottom: .5px solid black;
            }
            .double_row > span:nth-child(3) {
                border-left: .5px solid black;
            }
            .left {
                text-align: left !important;
            }
            .right {
                text-align: left !important;
                margin-left: 15em !important;
                font-weight: bold;
            }
            .teacher {
                position: absolute;
                font-size: .8em;
                margin-top: 92em;
                display: grid;
                grid-template-columns: 1fr 1fr 1fr 1.7fr;
                align-items: center;
                align-items: center;
                text-align: center;
                width: 100%;
                font-style: italic;
            }
            .teacher > div:first-child {
                text-align: left;
            }
            .teacher > div:not(:first-child) {
                display: grid;
                align-items: center;
                justify-content: center;
                width: 80%;
                padding-top: .5em;
                text-align: center;
                border-top: 1px;
                border-style: dotted none none none;
            }
        </style>
    </head>
    <body>
        <div id="print">
            <div class="container">
                <div class="heading">
                    <div class="heading_logo">
                        <img class="logo" src="logo.png">
                    </div>
                    <div class="heading_title">
                        <p style="font-size:1.2em; font-weight: bold;">SHAHJALAL UNIVARSITY OF SCIENCE & TECHNOLOGY SYLHET, BANGLADESH.</p>
                        <p style="font-size:1.15em;">Grade Certificte</p>
                        <p>B.Sc. in (Engg.) Examination</p>
                        <p>Session : 2018-19</p>
                    </div>
                </div>
                <div class="info">
                    <span>Institution</span><span>:</span><span>Sylhet Engineering College, Sylhet</span>
                    <span style="padding-bottom: .5em;">Department</span><span>:</span><span class="f">Computer Science & Engineering</span>
                    <span>Registration No.</span><span>:</span><span>2018331555</span>
                    <span>Student's Name</span><span>:</span><span>ABDULLAH AL NASEEH CHOWDHURY</span>
                </div>
                <div class="title_right">
                    <div class="title_right_container">
                        <span >Numeric Grade</span><span>Letter Grade</span><span>Grade Point</span>
                        <span>80% or above</span><span>A+</span><span>4.00</span>
                        <span>75% to less than 80%</span><span>A</span><span>3.75</span>
                        <span>70% to less than 75%</span><span>A-</span><span>3.50</span>
                        <span>65% to less than 70%</span><span>B+</span><span>3.25</span>
                        <span>60% to less than 65%</span><span>B</span><span>3.00</span>
                        <span>55% to less than 60%</span><span>B-</span><span>2.75</span>
                        <span>50% to less than 55%</span><span>C+</span><span>2.50</span>
                        <span>45% to less than 50%</span><span>C</span><span>2.25</span>
                        <span>40% to less than 45%</span><span>C-</span><span>2.00</span>
                        <span>less than 40%</span><span>F</span><span>0.00</span>
                    </div>
                </div>

                <div class="semester">
                    <div style="padding-top: 1.3em; padding-bottom: 1em; font-size: .8em; display: grid; grid-template-columns: 3fr 1fr;">
                        <div style="margin-left: 1.5em; font-weight: bold;">First Year First Semester 2017</div>
                        <div style="font-weight: bold;">Held on: September</div>
                    </div>
                    <div class="table">
                        <span>Course No.</span><span class="left">Course Title</span><span>Credit</span><span style="padding: 0;"><div class="double_row"><span>Grade Obtained</span><span>Grade Point</span><span>Letter Grade</span></div></span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span style="border: 0px !important"></span><span class="right">This Semester Total :</span><span>13.6</span><span>3.64</span><span>A+</span>
                        <span style="border: 0px !important"></span><span class="right">Comulative :</span><span>13.6</span><span>3.64</span><span>A+</span>
                    </div>
                </div>

                <div class="semester">
                    <div style="padding-top: 1.3em; padding-bottom: 1em; font-size: .8em; display: grid; grid-template-columns: 3fr 1fr;">
                        <div style="margin-left: 1.5em; font-weight: bold;">First Year First Semester 2017</div>
                        <div style="font-weight: bold;">Held on: September</div>
                    </div>
                    <div class="table">
                        <span>Course No.</span><span class="left">Course Title</span><span>Credit</span><span style="padding: 0;"><div class="double_row"><span>Grade Obtained</span><span>Grade Point</span><span>Letter Grade</span></div></span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span>CSE - 105</span><span class="left">Object Oriented Programming</span><span>2</span><span>3.00</span><span>B</span>
                        <span style="border: 0px !important"></span><span class="right">This Semester Total :</span><span>13.6</span><span>3.64</span><span>A+</span>
                        <span style="border: 0px !important"></span><span class="right">Comulative :</span><span>13.6</span><span>3.64</span><span>A+</span>
                    </div>
                </div>
                
                <div class="teacher">
                    <div style="font-size: .9em;">
                        <b>Printed on :</b> 20-Oct-22
                    </div>
                    <div>Prepared by</div><div>Compared by</div><div>Deputy Controller of Examination</div>
                </div>
            </div>
        </div>
        
    </body>
</html>
'''

import webbrowser
new = 2
url = "file:///C:/Users/USER/Desktop/result/demo.html"
webbrowser.open(url,new=new)