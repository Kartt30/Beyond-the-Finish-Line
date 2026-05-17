<?php
include "koneksi.php";

$nis=$_POST['Nis'];
$nama=$_POST['Siswa'];
$tglLahir=$_POST['Alamat'];
$alamat=$_POST['TempatLahir'];
$tempatLahir=$_POST['TanggalLahir'];

$simpan=mysqli_query($connect,"INSERT INTO siswa 
VALUES('$nis','$nama','$tglLahir','$tempatLahir','$alamat')");

if($simpan){
 echo "penyimpanan berhasil";
}else{
 echo "penyimpanan gagal";
}
?>