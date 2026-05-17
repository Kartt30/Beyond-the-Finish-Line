<html>

<head>
    <title>Data Siswa</title>
</head>

<body>
    <h3><b>Data Siswa</b></h3>
    <table border="1" width="90%">
        <tr>
            <td>No</td>
            <td>NIS</td>
            <td>Nama Siswa</td>
            <td>Alamat Tinggal</td>
            <td>Tempat Lahir</td>
            <td>Tgl Lahir</td>
        </tr>

        <?php
        include "koneksi.php";

        $sql = mysqli_query($connect, "SELECT * FROM Siswa");

        $no = 1;
        while ($data = mysqli_fetch_array($sql)) {
            $nis = $data['Nis'];
            $nama = $data['Siswa'];
            $alamat = $data['Alamat'];
            $tempat = $data['TempatLahir'];
            $tanggal = $data['TanggalLahir'];
        ?>

            <tr>
                <td><?php echo $no++; ?></td>
                <td><?php echo $nis; ?></td>
                <td><?php echo $nama; ?></td>
                <td><?php echo $alamat; ?></td>
                <td><?php echo $tempat; ?></td>
                <td><?php echo $tanggal; ?></td>
            </tr>
        <?php
        }
        ?>
    </table>
</body>

</html>