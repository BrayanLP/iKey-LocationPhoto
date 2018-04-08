
<h1>Standard Data</h1>
<?php
$exif = exif_read_data('1.jpg', 'IFD0');
echo $exif===false ? "No header data found.<br />\n" : "Image contains headers<br /><br />";

$exif = exif_read_data('1.jpg', 0, true);
foreach ($exif as $key => $section) {
    foreach ($section as $name => $val) {
        echo "$key.$name: $val<br />\n";
    }
}
?>
<br><br>
<h1>Print All Information</h1>
<?php
function arrayPrettyPrint($exif, $level) {
    foreach($exif as $k => $v) {
        for($i = 0; $i < $level; $i++)
            echo("&nbsp;");  
        if(!is_array($v))
            echo("<b>".$k ."</b> => " . $v . "<br/>");
        else {
            echo("<br><b>".$k . "</b> => <br/>");
            arrayPrettyPrint($v, $level+1);
        }
    }
}
arrayPrettyPrint($exif, 0);
?>
