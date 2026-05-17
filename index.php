<?php
include "koneksi.php";
?>

<htm>

    <head>
        <title>Document</title>
    </head>

    <body>
        <h2>Data Siswa</h2>
        <table border="1" width="100%">
            <tr>
                <td>No</td>
                <td>NIS</td>
                <td>Nama Siswa</td>
                <td>Alamat Tinggal</td>
                <td>Tempat Lahir</td>
                <td>Tgl Lahir</td>
            </tr>

            <?php
            $no = 1;
            $sql = mysqli_query($connect, "SELECT * FROM Siswa");

            while ($data = mysqli_fetch_array($sql)) {
                $nis = $data['Nis'];
                $nama = $data['Siswa'];
                $alamat = $data['Alamat'];
                $tempat = $data['TempatLahir'];
                $tanggal = $data['TanggalLahir'];

            ?>

                <tr>
                    <td><?php echo $no++; ?></td>
                    <td><?php echo $nis++; ?></td>
                    <td><?php echo $nama++; ?></td>
                    <td><?php echo $alamat++; ?></td>
                    <td><?php echo $tempat++; ?></td>
                    <td><?php echo $tanggal++; ?></td>
                </tr>
            <?php
            }
            ?>
        </table>
    </body>

    </html>