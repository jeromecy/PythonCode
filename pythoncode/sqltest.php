<!DOCTYPE html>
<html>
 <head>
  <title>PHP 测试</title>
 </head>
 <body>
<?php
$pdo = new PDO("mysql:host=qdm166846301.my3w.com;dbname=qdm166846301_db","qdm166846301","01240304");
if($pdo -> exec("insert into unionpay(date,base,transact,currency) values('2016-06-25','CNY','NZD',7.1286)")){
echo "ok";
echo $pdo -> lastinsertid();
}else {
    echo "Have a good night!";
}
?>
 </body>
</html>