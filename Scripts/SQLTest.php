<?php
$dbServerName = "192.168.10.46";
$dbUsername = "frollins";
$dbPassword = "R0b0t!cs";
$dbName = "nfsmssql";

// create connection
$conn = mysql_connect($dbServerName, $dbUsername, $dbPassword, $dbName);

// check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully </br>";

$db_selected = mysql_select_db('nfsmssql', $conn);
if (!$db_selected) {
    die ('Can\'t use DB : ' . mysql_error());
}
echo "Used $dbName Successfully </br>";


/*
 * get data from remote database table
 */

$query = 'SELECT * from webclientsite where SiteID like "%5%"';
$result = mysql_query($query, $conn);

// Check result
// This shows the actual query sent to MySQL, and the error. Useful for debugging.
if (!$result) {
    $message  = 'Invalid query: ' . mysql_error() . "</br></br>";
    $message .= 'Whole query: ' . $query;
    die($message);
}
 
 while($row = mysql_fetch_assoc($result)) {
	 echo "sName :{$row['sName']}, SiteID :{$row['SiteID']}  <br> ";
   } 
   echo "Fetched data successfully\n";
   mysql_close($conn);

?>

