
<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = $_POST["name"];
fwrite($myfile, $txt);
$txt = "\n";
fwrite($myfile, $txt);
fclose($myfile);
?>