<?php
include "koneksi.php";

$idBuku = $_POST['idBuku'];
$judul = $_POST['judul'];
$penulis = $_POST['penulis'];
$penerbit = $_POST['penerbit'];

$simpan = mysqli_query($connect, "INSERT INTO buku
VALUES('$idBuku','$judul','$penulis','$penerbit')");

if ($simpan) {
    echo "penyimpanan berhasil";
} else {
    echo "penyimpanan gagal";
}
