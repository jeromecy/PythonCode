<!DOCTYPE html>
<html>
<head>
<title>unionpay currency</title>
</head>
<body>
<?php
    // by MoreWindows( http://blog.csdn.net/MoreWindows )
    //定义常量
    define(DB_HOST, 'uniontokyo.cg6x01smgrfp.ap-northeast-1.rds.amazonaws.com');
    define(DB_USER, 'victorcraft');
    define(DB_PASS, 'ilove86415175');
    define(DB_DATABASENAME, 'unionmysql');
    define(DB_TABLENAME, 'unionpay');
    
    
    //数据库表的列名
    $dbcolarray = array('ID', 'date', 'base', 'transact','currency','weekdays');
    
    //mysql_connect
    $conn = mysql_connect(DB_HOST, DB_USER, DB_PASS) or die("connect failed" . mysql_error());
    mysql_select_db(DB_DATABASENAME, $conn);
    //读取表中纪录条数
    $sql = sprintf("select count(*) from %s", DB_TABLENAME);
    $result = mysql_query($sql, $conn);
    
    $sql2 = sprintf("select count(*) from %s where `currency`=0", DB_TABLENAME);
    $result2 = mysql_query($sql2, $conn);
    
    //$sql3 = sprintf("select * from %s where `base`=\"CNY\" and `transact`=\"NZD\" ORDER BY `date` desc", DB_TABLENAME);
    //$result3=mysql_query($sql3, $conn);
    
    if ($result)
    {
        $count = mysql_fetch_row($result);
        $count2 = mysql_fetch_row($result2);
        //    $count3 = mysql_fetch_row($result3);
    }
    else
    {
        die("query failed");
    }
    //echo "there are $count[0] data in sql and $count2[0] are 0 currency <br />";
    echo "there are $count[0] data set and $count2[0] are 0<br />"
    
    //$sql = sprintf("select %s from %s", implode(",",$dbcolarray), DB_TABLENAME);
    //$result = mysql_query($sql, $conn);
    
    //echo '<table id="tab" border=l>'
    //echo "<tr>"
    //$count3[0]
    //echo "</tr>"
    //echo '</table>'
    
    //表格
    //echo '<table id="Table" border=1 cellpadding=10 cellspacing=2 bordercolor=#ffaaoo>';
    //表头
    //$thstr = "<th>" . implode("</th><th>", $dbcolarray) . "</th>";
    //echo $thstr;
    //表中的内容
    //while ($row=mysql_fetch_array($result3, MYSQL_ASSOC))//与$row=mysql_fetch_assoc($result)等价
    //{
    //  echo "<tr>";
    //  $tdstr = "";
    //  foreach ($dbcolarray as $td)
    //      $tdstr .= "<td>$row[$td]</td>";
    //  echo $tdstr;
    //  echo "</tr>";
    //}
    //echo "</table>";
    mysql_free_result($result);
    mysql_free_result($result2);
    //mysql_free_result($result3);
    mysql_close($conn);
    ?>
</body>
</html>