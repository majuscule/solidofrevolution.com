<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
  <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
  <script type='text/javascript' src='/jquery.js'></script>
  <script type='text/javascript' src='/validate.js'></script>
  <title>solidofrevolution</title>
</head>

<body>

<pre>
usage: solid.py [-h] [-axis {x,y}] [-o #] [-m {d,s}] [-g] [-v]
                {x,y} = equation a b

Find the volume of the solid of rotation defined. The * symbol must be used
for multiplication, and ** to raise a power. Trailing .0's must be used for
constants. Answers are accurate to 6 decimals.

example:
  ./solid.py x**2-2*x-12 0 1

positional arguments:
  {x,y}        x|y
  =
  equation     continous function
  a            bound 'a'
  b            bound 'b'

optional arguments:
  -h, --help   show this help message and exit
  -axis {x,y}  axis of revolution (default == x)
  <s>-o #         offset axis by # (default == 0)</s>
  <s>-m {d,s}     method (disk/shell)</s>
  <s>-g           show function graph</s>
  <s>-v           verbose (for debugging)</s>
</pre>

<br>

<form id="calulator" action="calculate" method="post" > 
  <input type="radio" id="dependent_variable" name="dependent_variable" value="x" disabled="true"/> x
  <input type="radio" id="dependent_variable" name="dependent_variable" value="y" /> y
  &nbsp; &nbsp;
  =
  &nbsp; &nbsp;
  <input type="text" id="equation" name="equation" />
  <br> <br>
  revolved about
  <br> <br>
  <input type="radio" name="axis_of_revolution" value="x" /> x
  <input type="radio" name="axis_of_revolution" value="y" /> y
  <br> <br>
  with bounds
  <br> <br>
  a = <input id="a" type="text" style="width:30px;" name="a" />,
  b = <input id="b" type="text" style="width:30px;" name="b" />
  
  <br> <br> <br>
  <input type="submit" value="./calculate" id="submit" />
</form> 

</body>

<br>
<h2><a href="http://dylansserver.com">dylansserver.com</a>, <a href="mailto:dylan@psu.edu">dylan@psu.edu</a>
</h2>

</html>
