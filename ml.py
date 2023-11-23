# Import library
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk 
import pandas as pd
import string
import re
import matplotlib.pyplot as plt

data = [
#Dinas Sumberdaya Air dan Bina Marga Kota Bandung
    {"text": "Rusaknya Jalan Di Jl. Gatot Subroto Dari Simpang Lima Hingga Simpang Jl. Malabar Kota Bandung Rusaknya jalan dari jalan gatot subroto, terutama dari simpang lima hingga simpang jl. malabar. telah dilampirkan juga bukti foto jelas pada lampiran dibawah. tetapi hanya bagian simpang malabar saja, sedangkan bagian lain tidak sempat. dinas terkait bisa mengadakan survei dahulu mana saja bagian yg", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Saluran Air Tersumbat Mohon dibersihkan oleh dinas terkait ,saluran air tersumbat di persimpangan jl.dr.wahidin - jl.dr.rum (depan rumah nomor 5 dan 7), posisi di kota bandung ,kelurahan pasirkaliki kecamatan cicendo.saluran ini sudah diperbaiki oleh dinas bina marga namun sayang aliran air tidak berfungsi", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Jalan Rusak Bergelombang Jl. Gatot Subroto Dari Simpang Jl. Laswi Hingga Simpang Jl. Maleer Iii Kepada dinas terkait yg berwenang silahkan mengadakan survei kondisi yang sangat memprihatinkan dari jl.gatot subroto, khususnya dari simpang jl. laswi hingga simpang jl. maleer iii. jalan ini mengalami banyak masalah, seperti permukaan bergelombang, aspal terkelupas, tambalan yang bergelombang,", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Permohonan Perbaikan Jalan Pemukiman Warga Yang Rusak Permohonan perbaikan jalan warga yang rusak part 4selamat pagi kepada instansi dan lembaga yang terkait untuk menangani masalah ini kami atau saya pribadi yang menyampaikan tentang kerusakan jalan ini,meminta agar segera dilakukan perbaikan di jl mutiara 4 bandung kelurahan turangga", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Jalan Berlubang Mohon dibantu pinggir jalan / trotoar berlubang lumayan cukup dalam . posisi dekat griya pahlawan", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Saluran Air Tidak Kunjung Diselesaikan Lokasi: jalan terusan pesantren, rt04 rw11, sukamiskin, arcamanik, kota bandung kronologi: pengerjaan saluran air dengan menggali parit dan membongkar akses masuk ke rumah warga dilakukan kira2 pada pertengahan juli 2023, hingga kini galian tsb tidak diselesaikan.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Lantai Trotoar Pecah Assalamualaikum wr. wb sampurasun", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Plat Beton Penutup Saluran Air Ambrol Ijin lapor lubang di jalan dursasana seberang tps pasar pamoyanan. akibat sering dilewati mobil gara2 bak sampahnya agak ditengah jalan dan akibat kena beban backhoe waktu pengangkutan sampah hari sabtu 9/9/2023", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Laporan Kerusakan Jembatan Jalan Terjadi retak jembatan penghubung jalan di jln sukarma, kecamatan bojongloa kaler, kelurahan babakan asih. kode pos 40232. mohon bantuannya.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Lubang Di Jl. Suniaraja, Belokan Sebelum Masuk Jl. Pasar Barat Kami ingin melaporkan adanya lubang besar di jl. suniaraja, tepatnya pada belokan sebelum masuk jl. pasar barat. lubang ini merupakan potensi bahaya bagi pengguna jalan dan kendaraan yang melintas.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Kerusakan Jalan Ada jalan amblas, berlubang cukup besar di jl. lengkong besar no.42 bandung", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Pengaspalan Ulang Flyover Pelangi Mohon untuk dilakukan pengaspalan ulang pada flyover pelangi antapani, bandung dikarenakan aspal flyover tersebut tidak rata dan membuat pengendara motor kesulitan untuk bermanuver dengan stabil, terutama dari arah jl. jakarta menuju jl. trs. jakarta di sisi paling kiri. terima kasih.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Saluran Air Tidak Kunjung Diselesaikan Lokasi: jalan terusan pesantren, rt04 rw11, sukamiskin, arcamanik, kota bandung kronologi: pengerjaan saluran air dengan menggali parit dan membongkar akses masuk ke rumah warga dilakukan kira2 pada pertengahan juli 2023, hingga kini galian tsb tidak diselesaikan. warga kesulitan keluar masuk rumah terlebih ada lansia yang jika ada keadaan darurat akan sulit untuk keluar rumah. update 23 sep: dari informasi pak rw kami pada 22 sep, pekerjaan tidak dapat dilanjutkan pada tanggal 23 sep karena pergantian kepada pemborong awal bernama soni. pemborong bernama soni ini yang menyebabkan pekerjaan terkatung-katung selama 2 bulan. pekerjaan sempat dilakukan oleh pemborong lain, namun kenapa harus kembali kepada pemborong lama yang tidak jelas pekerjaannya. mohon perhatiannya, kami sangat terganggu dengan situasi ini. kami sudah cukup bersabar dengan situasi ini, maka sekali lagi kami harap bisa segera diselesaikan.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Gorong-Gorong Rusak Tutup gorong-gorong di jalan gatot subroto rusak membahayakan pejalan kaki. tepatnya di sebrang bengkel iphone gatot subroto bandung", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Tutup Saluran Air Tengah Jalan Rusak, Membahayakan Mohon bantuan perbaikan tutup saluran air di tengah jalan dr. setiabudi arah cihampelas. list besi mencuat, bisa merusak roda atau melukai pengendara khususnya motor. foto maps lokasi dan kerusakan yang dimaksud terlampir. mohon bantuan segera, karena sudah terpantau 2 minggu tidak ada perubahan. terima kasih.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Pelebaran Jalan Dan Jembatan Di Kota Bandung Selamat malam, ini dengan warga bandung, mau menyampaikan mengenai jalan-jalan di kota bandung, terutama di jalan terusan psm, jalan cidurian, jalan kawaluyaan kiaracondong, jalan gatot subroto dari blk bandung sampai jembatan sungai, jalan terusan babakan sari kiaracondong, jalan di samping fly over jalan jakarta - jalan supratman, jalan di samping fly over antapani, dsb. untuk bisa dilakukan pelebaran jalan dan jembatan karena jalan-jalan yang disebutkan tadi sering menimbulkan kemacetan karena penyempitan jalan, terutama di jam-jam sibuk dan kalau ada satu kendaraan yang parkir bisa menimbulkan kemacetan. dimohon untuk segera dilakukan pelebaran jalan dan jembatan karena bisa menimbulkan kemacetan parah. proyek double track/jalur ganda ka kiaracondong-cicalengka aja bisa. masa pelebaran jalan di kawasan bandung timur ngak bisa. supaya bisa dilakukan pelebaran jalan dan jembatan secepatnya. dan juga untuk jalan terusan buah batu, jalan terusan mohammad toha, jalan terusan kopo juga dilebarkan karena sering menimbulkan kemacetan. mohon segera direalisasikan pelebaran jalan supaya mengurai kemacetan yang sudah cukup dan sangat parah. dan juga relokasi bangunan yang terdampak pelebaran jalan juga harus jadi perhatian. supaya tidak ada yang dirugikan. terima kasih.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Drainase Bawah Beton Mampet Dan Keluar Air Kotor Hitam Di Jalan Gelap Nyawang Selokan bawah beton mampet dan keluar air kotor hitam di jalan gelap nyawang depan bmg itb", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
#Dinas Perhubungan Kota
    {"text": "Parkir Mobil Di Atas Jembatan Cikapundung Acara Di Sabuga ItbMohon dishub dapat menertibkan parkir mobil di sepanjang jembatan cikapundung jl. siliwangi, terkait ada acara di sabuga itb. acara pagi ini sabtu 11 november 2023karena selain mengganggu lalin yang lebih bahaya adalah merusak fungsi jembatan yang sudah cukup tua dibangun akan rusak oleh beban parkir mobil yang ada di atasnya.haturnuhun", "category": "Dinas Perhubungan Kota"},
    {"text": "Tombol Pejalan Kaki Tidak BerfungsiAssalamualaikum wr. wbyth. pj. walikota bandungbahwa tombol pejalan kaki tidak berfungsi, mohon untuk diperbaiki agar bisa digunakan kembali.terima kasihwassalamualaikum wr. wb sumber video:https://photos.app.goo.gl/x1tbq6fnwbefpgdba", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Tombol Penyebrangan Jalan MatiAssalamualiakum wr. wbyth pj. walkot bandungbahwasanya lampu penyebrangan jalan mati/rusak, mohon untuk memperbaiki lampu tersebut agar bisa digunakan kembaliterima kasihwassalamualaikum wr. wb lokasi : depan masjid raya bandung", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Penerangan Jalan Mati Lampu penerangan jalan di jalan gedebage selatan sekitar kantor kecamatan sudah seminggu mati mohon perhatiannya!", "category": "Dinas Perhubungan Kota"},
    {"text": "Persimpangan Melawan Arus Membahayakan Di Cijerah & Jl Jend SudirmanTolong kepada yg berwenang untuk diadakannya kembali (dulu pernah ada) pembatas tengah (yg saya tandai warna hijau pada foto) agar tidak ada pemotor yg mememotong jalur karena sangat membahayakan dan sering ada yg senggolan/kecelakaan, selain itu juga sering menimbukan kemacetan, jangan sampai menunggu ada korban jiwa baru ditindak. mohon tindakannya segera terimakasih.sebagai tambahan kalau bisa dibuat permanen atau bahannya jangan tali pasti akan ada yg gunting.", "category": "Dinas Perhubungan Kota"},
    {"text": "Parkir Di Area Kampus Itb GaneshaSelamat pagi/siang/sore/malam, perkenalkan saya kebetulan seorang mahasiswa yang sedang menempuh pendidikan di kampus itb ganesha yang berasal dari luar bandung. saya izin bertanya mengenai manajemen parkir yang ada di sekitar area kampus itb (terutama jl. skanda dan jl. gelap", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Pju Jalan Kecubung Bandung Mati Lampu pju jalan kecubung antara rumah no 12 da 14 mati total , sehingga rumah disekitarnya gelap. mohon bantuannya untuk ditindaklanjuti", "category": "Dinas Perhubungan Kota"},
    {"text": "Informasi Lowongan Magang Selamat sore, izin bertanya apakah dinas perhubungan kota bandung membuka lowongan magang bagi mahasiswa fresh graduated lulusan s1 perencanaan wilayah dan kota?", "category": "Dinas Perhubungan Kota"},
    {"text": "Minim Penerangan Jalan Assalamualaikum, ijinkan saya sebagai warga menyampaikan keprihatinan pada kondisi jalan yang ramai tetapi minim penerangan di jl.bukit jarian kota bandung, jalan tersebut banyak aktivitas mahasiswa dan juga warga serta pengunjung rumah sakit tetapi tidak ada lampu penerangan yang memadai mulai dari pertigaan bukit jarian-ciumbuleuit s/d rumah sakit paru rotinsulu. mohon sekiranya mendapatkan atensi dari dinas terkait agar menambah lampu yang ada. saat ini ada pjl swadaya masyarakat yang menggunakan tenaga surya tetapi tidak efektif, jika sekiranya dapat diganti dengan listrik dan lampu led pju akan lebih baik agar wilayah tersebut terang. hatur nuhun", "category": "Dinas Perhubungan Kota"},
    {"text": "Biaya Parkir Tidak Berdasarkan Aturan Yang Berlaku Parkir di sebrang pasar kiaracondong, dan membawa mobil tipe innova lalu parkir 1 jam, dikenakan biaya 15rb, dan tukang parkir menggunakan kuitansi yang sudah di cap bertuliskan dishub. tolong di tertibkan pungli seperti ini, ditambah sudah merusak citra dishub dengan mencantumkan dishub di cap kuitansinya, saya memiliki bukti berupa foto.", "category": "Dinas Perhubungan Kota"},
    {"text": "Parkir Mobil Di Atas Jembatan Cikapundung Acara Di Sabuga Itb Mohon dishub dapat menertibkan parkir mobil di sepanjang jembatan cikapundung jl. siliwangi, terkait ada acara di sabuga itb. acara pagi ini sabtu 11 november 2023karena selain mengganggu lalin yang lebih bahaya adalah merusak fungsi jembatan yang sudah cukup tua dibangun akan rusak oleh beban", "category": "Dinas Perhubungan Kota"},
    {"text": "Tombol Pejalan Kaki Tidak Berfungsi Assalamualaikum wr. wb yth. pj. walikota bandung Lampu Penerangan Jalan Mati ampu penerangan jalan di jalan gedebage selatan sekitar kantor kecamatan sudah seminggu mati mohon perhatiannya!", "category": "Dinas Perhubungan Kota"},
    {"text": "Persimpangan Melawan Arus Membahayakan Di Cijerah & Jl Jend Sudirman Tolong kepada yg berwenang untuk diadakannya kembali (dulu pernah ada) pembatas tengah (yg saya tandai warna hijau pada foto) agar tidak ada pemotor yg mememotong jalur karena sangat membahayakan dan sering ada yg senggolan/kecelakaan, selain itu juga sering menimbukan kemacetan, jangan sampai menunggu ada korban jiwa baru ditindak. mohon tindakannya segera terimakasih. sebagai tambahan kalau bisa dibuat permanen atau bahannya jangan tali pasti akan ada yg gunting.", "category": "Dinas Perhubungan Kota"},
    {"text": "Parkir Di Area Kampus Itb Ganesha Selamat pagi/siang/sore/malam, perkenalkan saya kebetulan seorang mahasiswa yang sedang menempuh pendidikan di kampus itb ganesha yang berasal dari luar bandung. saya izin bertanya mengenai manajemen parkir yang ada di sekitar area kampus itb (terutama jl. skanda dan jl. gelap nyawang) yang kebetulan saat ini sebagai satu-satunya opsi tempat parkir kendaraan mobil bagi mahasiswa yang tidak kebagian parkir di area itb. apakah di area jl. skanda dan jl. gelap nyawang ini dikelola oleh petugas parkir yang terdaftar resmi dari dishub bandung atau tidak? sebab saya seringkali melihat tukang parkir yang berjaga di sekitar area ini sangat banyak jumlahnya berjejeran walaupun masih di satu area saja dan beberapa dari mereka bahkan tidak menggunakan rompi petugas parkir dishub. belum lagi terkadang mereka mematok parkir yang seenaknya saja bahkan ada aturan yang menurut saya tidak masuk akal dimana kejadian ini dialami oleh teman saya yang membawa kendaraan. kebetulan saat itu saya dan teman saya secara terpaksa harus parkir di area jl. skanda sekitar pukul 14.00 wib untuk ke kampus dan dimintai tarif parkir sebesar rp10.000. setelah itu, kami pulang dari kampus sekitar pukul 5-6 sore dan kebetulan di saat itu juga dimintai uang parkir kembali dengan alasan tukang parkir yang berjaga beda shift. saat itu kami dimintai parkir kembali sebesar rp5.000. jujur saya sangat miris dengan manajemen parkir yang ada di area ini yang saya yakini sebagian besar dikelola oleh ormas/preman yang berkedok menjadi tukang parkir dengan mental miskin hanya meminta-minta di lahan umum. oleh karena itu, saya sangat mohon kepada para bapak/ibu yang memiliki kewenangan di dishub bandung agar lebih memberikan perhatian lebih dan benar-benar bisa mengalokasikan petugas resmi serta menindak tegas para petugas2 yang meresahkan agar pengelolaan parkir di kota bandung ini bisa lebih terkelola dengan baik dengan manajemen yang teratur. saya sebagai mahasiswa yang membawa kendaraan juga setiap hari harus menghadapi kejadian2 seperti ini mengingat itb sendiri kurang memperhatikan demand parkir mobil para mahasiswanya. oleh karena itu, saya sangat mohon atas perhatiannya terkait pengelolaan parkir di sekitar area kampus itb ini. terimakasih.", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Pju Jalan Kecubung Bandung Mati Lampu pju jalan kecubung antara rumah no 12 da 14 mati total , sehingga rumah disekitarnya gelap. mohon bantuannya untuk ditindaklanjuti", "category": "Dinas Perhubungan Kota"},
    {"text": "Informasi Lowongan Magang Selamat sore, izin bertanya apakah dinas perhubungan kota bandung membuka lowongan magang bagi mahasiswa fresh graduated lulusan s1 perencanaan wilayah dan kota?", "category": "Dinas Perhubungan Kota"},
    {"text": "Minim Penerangan Jalan Assalamualaikum, ijinkan saya sebagai warga menyampaikan keprihatinan pada kondisi jalan yang ramai tetapi minim penerangan di jl.bukit jarian kota bandung, jalan tersebut banyak aktivitas mahasiswa dan juga warga serta pengunjung rumah sakit tetapi tidak ada lampu penerangan yang memadai mulai dari pertigaan bukit jarian-ciumbuleuit s/d rumah sakit paru rotinsulu. mohon sekiranya mendapatkan atensi dari dinas terkait agar menambah lampu yang ada. saat ini ada pjl swadaya masyarakat yang menggunakan tenaga surya tetapi tidak efektif, jika sekiranya dapat diganti dengan listrik dan lampu led pju akan lebih baik agar wilayah tersebut terang. hatur nuhun", "category": "Dinas Perhubungan Kota"},
#Dinas Kependudukan dan Pencatatan Sipil Kota Bandung
    {"text": "Nik Tidak Sesuai Dengan No Kk Nik 3273042609040010 no kk 3273042101190005 tidak sesuai dengan no kk, padahal satu no kk", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Pencetak Ulang Ktp Sudah 1bulan lebih masih aja belum beres2 cetak ulang ktp.. pelayanan nya kurang baik.. sudah di tanya via w.a tapi tidak ada jawaban lagi..", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Kartu Keluarga 4 Bulan Belum Jadi ? Saya mau lapor kartu keluarga saya belum jadi dari bulan april sampai dengan bulan agustus sekarang apalagi ktp saya cek langsung di sipaku. apakah ada sesuatu yang tidak diketahui atau di tutup tutupin orang awam seperti saya ? jangan saling menutupi. apakah harus ada kenalan atau bayar ??? itu kan gratifikasi. kalau bayar memang ada perdanya ? tolong menjadi perhatian !!! jejak digital bisa viral dan susah hilang. jangan saling lempar antara disdukcapil dan kecamatan ataupun sebaliknya. tolong ditindak langsung!!", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Pencetakan Kartu Keluarga Lama Assalamu'alaikum wr wb, saya adalah warga kecamatan cibeunying kaler kebetulan sudah 2 bulan pembuatan kartu keluarga saya belum selesai, padahal kata petugas 8 hari bisa di konfirmasi, petugas berdalih karena kewenangan itu dari disduk jadi terlambat, tolong ini bagaimana penyelesaiannya", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Legalisir Dokumen Kependudukan Selamat pagi saya mau bertanya terakit legalisir dokumen seperti akte kelahiran dsb. yang dibuat bukan di kota bandung apakah harus ke kota kelahiranya? meningat saya sekarang warga kota bandung (ktp kota bandung). sepengetahuan saya dari dirjen disdukcapil (prof zudan) sudah mengatakan bahwa dapat melakukan legalisir atau berbasis domisili. tetapi masih ditolak oleh petugas satpam dan petugas loket meminta dan meminta surat keabsahan dari disduk asal padahal kami sudah melampirkan dokumen asli dan harus mengemail ke disdukcapil kota asal. mohon ditindaklanjuti oleh instansi terkait (disdukcapil kota bandung) yang bersatatus pelayanan prima kemenpan rb cc: dirjen disdukcapil kemendagri, kemenpan rb", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Kesalahan Nik Di Kip Selamat pagi dengan ini saya bermaksud menyampaikan bahwa ada kesalahan penulisan nik di kip milik anak saya yang bernama: nira sari pramudita nisn: 010347376 asal sekolah sdn pabaki bandung. sekarang di smp pahlawan toha bandung. pada kip tertera nik: 3273045711100001. nik tersebut tidak sesuai dengan kk dan dtks yang seharusnya 3273045712100004. dan hal ini menyebabkan bantuan tunai nya menjadi tidak cair. sebab itu saya harap permasalahan ini segera diperbaiki, supaya bantuan tunainya cair kembali, karena kami sangat membutuhkan bantuan tersebut. demikian yang ingin saya sampaikan. terima kasih. wassalam ", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Terjadi Tindak Pidana Pemalsuan Data Kewarga Negaraan Telah terjadi tindak pidana pemalsuan akte lahir dimana orang yang bernama kevin dan eunice..mereka lahir di kota deventer, belanda dan telah mempunyai akte lahir disana.. mereka memalsukan keterangan dengan mengaku lahir di kota bandung, indonesia", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Blangko Ktp Habis Terus Ketika anak saya hendak membuat ktp dari tgl 27 jun 2023 sampai dgn sekarang diinfonya blangkonya kosong . padahal secara ketentuan max 2 minggu sudah selesai . apakah memang tidak tersedianya blangko? atkah kenapa ya?", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Disdukcapil Kota Bandung Tidak Informatif Kepada yth disdukcapil kota bandung", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Legalisir Akta Kelahiran Selamat siang, perkenalkan saya tunggara rochman dengan pemilik ktp domisili kota bandung, jawa barat. saya lahir", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Membuat Kartu Keluarga setelah menikah Selamat pagi,Mau bertanya, saya baru menikah di november 2022 kemarin.Status:Saya (mempelai pria) berdomisili di Kabupaten Bandung, dan 1 KK dengan ayah saya.Istri berdomisili di Kota Bandung, dan 1 kk dengan ayah, ibu, dan adiknya.Setelah menikah saya dan istri tinggal di rumah saya yang", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Pengurusan Ktp Lama Sekali Utk Ganti Ktp Yang Rusak Kepada pemda kota bandung dinas kependudukan mengapa utk memperbarui ktp yang rusak tidak jelas hurupnya memakan waktu lama sekali,", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Proses Pembbuatan Kartu Keluarga 22 hari sudah saya menunggu pembuatan kk yang tidak selesai sampai saat ini, entah dari kecamatan coblong atau memang dari para pns di kota bandung yang mengurus kk tidak becuss !!! berikut no registrasi kk saya yang dari tgl 31 oktober belum selesai", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Pembuatan Akta Kelahiran Apa perlu surat pengantar rt dan rw kalau mau bikin akta kelahiran ?", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Pengajuan Dokumen Perpindahan & Kartu Keluarga Tidak Ada Di Email Selamat siang, saya mewakili orangtua saya mengurus dokumen perpindahan penduduk dan kartu keluarga melalui aplikasi salaman. di aplikasi status dokumen sudah selesai diproses dan dapat dicetak mandiri namun tidak ada email dari siakonline@dukcapil.kemendagri.go.id masuk. bagaimana", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Nik Yang Tidak Ada Di Kepegawaian Selamat malam izin bertanya kenapa nik saya tidak bisa tercatat dibadan kepegawaian? ini nik saya pak 3273045905970002", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Dokumen pisah KK Selamat pagi,Mohon infonya, apa saja tahapan dan dokumen yang dibutuhkan untuk pisah KK? Kami berencana untuk pindah ke luar Kota Bandung.Kami tunggu info selanjutnya.Terima kasih.", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Permohonan Pindah Kartu keluarga Selamat pagi admin Dukcapil Bandung, Saya Annisa Arnizanthya, WNI pemegang KTP dan KK Yogyakarta, saat ini ingin melakukan pindah KK ke Antapani Bandung. Apakah bisa dilaksanakan secara online? Dan mohon info untuk persyaratannya. Terima kasih.", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "PROBLEM PAS BUAT NPWP Assalamualaikum,Saya sedang menguruskan NPWP,Ketika registrasi Nomor NIK dan KK sudah saya input ternyata yang keluar nama orang lain, bagaimana solusinya.", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
    {"text": "Dokumen pisah KK Selamat pagi,Mohon infonya, apa saja tahapan dan dokumen yang dibutuhkan untuk pisah KK? Kami hendak pindah ke luar Kota Bandung.Kami tunggu info selanjutnya.Terima kasih.", "category": "Dinas Kependudukan dan Pencatatan Sipil Kota Bandung"},
#Satuan Polisi Pamong Praja Kota Bandung
    {"text": "Laporan #6858508 Tidak Ada Tindak Lanjut Oleh Kecamatan Astana Anyar Laporan #6858508 mengenai pedagang kaki lima di trotoar dan alat peraga kampanye pada fasilitas umum di persimpangan otista - pungkur yang di disposisikan ke kecamatan astana anyar tidak ada tindak lanjut sampai ditutup oleh admin padahal masalah belum selesai", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Pengawasan Perijinan Tugas Siapa? Selamat pagi sy ingin memberikan pengaduan atas kegiatan usaha yang merugikan lingkungan sekitar, kemudahan pemebrian ijin tentunya harus didampingi dengan perlindungan lingkungan", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Banyak Gelandangan Kalau Di Malam Hari, Di Siang Hari Ada Gerobak Dagang Menutupi Toko Banyak gelandangan kalau di malam hari, di siang hari ada gerobak dagang menutupi toko di jalan otista sekitar no 343 - 349", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Belviu Hotel Buat Kegaduhan Malam Tanggal 5 september 2023, belviu hotel bandung dan satpol pp kota bandung melakukan perjanjian tertulis tentang tidak ada kegiatan live music di roof top atas laporan warga, namun malam ini pihak belviu kembali mengadakan kegiatan tersebut seolah menyepelekan juga penjanjian dengan satpol pp kota bandung.", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Penertiban Pkl Yang Memakan Badan Jalan & Membuat Macet Setiap Hari Kepada satpol pp tolong tindakannya untuk beberapa pkl yang posisinya memakan jalan di kanan sepanjang jl kebon jati terutama di pertigaan menuju jl waringin, gereja bethel indonesia. apabila sulit untuk menindak menertibkan mungkin agar diberikan himbauan agar mempersiapkan dagangan jgn pada saat sore hari jam pulang kerja (after office hour) pukul 17.00 - 19.00 karena sangat membuat kemacetan bersamaan dengan masyarakat yang pulang bekerja. selain itu juga ditambah yg membuat macet adalah parkir sebelah kiri (pengunjung & bongkar muat pedagang) di sekitar pertigaan tersebut yg membuat jalan menyempit seperti kerucut. Tutup", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Tindakan Mendesak Terhadap Keberadaan Bendera Partai Yang Mengganggu Ketertiban Di Belokan Jl Waas Dan Persimpangan Batununggal - Soetta Kepada dinas yang berwenang, tanggal 13 september 2023 ijin melaporkan adanya keluhan terkait bendera partai politik yang terus terpasang di fasilitas umum di belokan jl waas dan persimpangan batununggal - soetta. hal ini telah mengganggu pemandangan dan ketertiban di kedua lokasi tersebut. sebagai bukti, kami telah melampirkan tangkapan layar dari cctv atcs yang menunjukkan adanya bendera-bendera tersebut. kami memohon kepada dinas yang berwenang untuk segera menertibkan dan menindaklanjuti laporan ini. langkah pemeriksaan rutin sangat diperlukan guna memastikan keindahan kota dan ketertiban fasilitas umum tetap terjaga. terima kasih atas perhatian dan tindakan yang akan diambil. hormat kami,", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Pemasangan Baliho Kampanye Ilegal Pada Fasilitas Umum Di Persimpangan Jl. Buah Batu - Jl Pelajar Pejuang Mohon tertibkan pemasangan baliho kampanye ilegal pada fasilitas umum di persimpangan jl. buah batu - jl pelajar pejuang karena sangat mengganggu kenyamanan dan pemandangan kota jd kumuh terlihat juga pada rekaman live cctv atcs terdapat banyak bendera", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Spanduk Bendera Partai Di Simpang Martanegara & Simpang Lingkar-Buah Batu Mengganggu Pemandangan Dan Ketertiban Kota Bandung Kami ingin melaporkan bahwa bendera partai politik terus terpasang di fasilitas umum di simpang martanegara & simpang lingkar-buah batu. penempatan ini telah mengganggu pemandangan dan ketertiban di kedua lokasi tersebut. sebagai bukti, kami telah melampirkan tangkapan layar dari diskominfo yang menunjukkan keberadaan bendera-bendera tersebut. kami mohon agar dinas yang berwenang segera menertibkan dan menindaklanjuti laporan ini dengan melakukan pemeriksaan rutin guna memastikan keindahan kota dan ketertiban fasilitas umum tetap terjaga.", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Bendera Dan Apk Pada Fasilitas Umu Di Persimpangan Jl Malabar Gatsu Mohon tindakannya ada bendera dan apk pada fasilitas umum di persimpangan jl malabar gatsu umum merusak keindahan dan ketertiban, silahkan di cek di ke 4 sisinya sangat membuat kumuh lampiran bukti foto terlampir", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Zona Merah Pkl Jadi Zona Pink?Assalamualaikum... sy warga rw03 kelurahan cijagra. mengucapkan terima kasih kepada pemkot bandung yg telah mengembalikan kembali fungsi trotoar di", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Spanduk Liar Di Sekitar Simpang Exit Gerbang Tol Pasteur & Jpo Btc Jl Pasteur Saya sebagai warga masyarakat ingin memberikan laporan mengenai temuan spanduk liar di simpang exit tol pasteur pada hari ini. saya telah mendapatkan bukti keberadaan spanduk tersebut melalui rekaman cctv atcs live yang saya miliki. hal ini menjadi perhatian saya karena melanggar peraturan", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Reklame Mengganggu & Merusak Keindahan Kota Bandung Di Persimpangan Jl. Aceh Saya melaporkan adanya baliho/spanduk mengganggu dan merusak keindahan di persimpangan jl.aceh. reklame ini menyebabkan kerusakan visual, pencemaran visual, dan pelanggaran peraturan tata kelola reklame. mohon penertiban dan pengawasan rutin untuk menjaga keindahan kota. berikut", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Baliho Partai Sudah 1 bulan berdiri. maaf tolong ini balohonya dicabut ya. trotoar minim. sering sekali untuk baliho partai. kalau tiba tiba hujan angin besar bisa menimpa pejalan kaki atau pengendara roda 2 dan 4. di jl. ahmad yani no. 224 kota bandung sebelum rel cikudapateuh kalau dari arah cicaheum. terimakasih", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Spanduk Iklan & Alat Peraga Kampanye Ilegal Di Simpang Masuk Tol Jl Terusan Pasir Koja - Jl Soekarno-Hatta Saya melaporkan adanya spanduk iklan & alat peraga kampanye ilegal di ke 4 sisi persimpangan masuk tol jl terusan pasir koja - jl soekarno-hatta yang melanggar aturan terkait waktu, tempat, dan jenis peragaan kampanye. spanduk-spanduk ini berisi gambar, nama, dan simbol dari seorang", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Iklan Di Trotoar Trotoar untuk pejalan kaki tolong jangan dibuat untuk iklan ini itu .. mengurangi space pejalan kaki. tolonglah mau pasang iklan di tempatnya yg sudah di sediakan. jng memanfaatkan fasilitas yg bukan tempatnya. tolong untuk pihak satpol-pp untuk menghilangkan", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Gangguan Pengamen warga merasa berisik gangguan suara musik keras dari pengamen jalanan memakai speaker setiap hari pagi sampai malam nonstop dan ada yang melindungi. lokasi di lampu merah sudirman astana anyar bandung", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Bendera Partai Bertebaran Sepanjang Jalan Layang Prof. Dr. Mochtar Kusumaatmadja / Pasoepati Merusak Pemandangan Jdi Kumuh Ijin melapokan terkalit bendera partai bertebaran sepanjang jalan layang prof. dr. mochtar kusumaatmadja / pasoepati merusak pemandangan jdi kumuh, di foto hanya sebagian, bendera ada di kedua arah dari ujung ke ujung jalan layang walau tidak full tapi sangat mengganggu keindahan", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Cafe 24 Jam Mengganggu Ketertiban Cafe dreams di jalan ir. h. juanda 286 sangat mengganggu ketertiban dan kenyamanan area, sampai jam 1 malam masih live music keras sekali, area outdoor tidak ada peredaman sama sekali. mau sampai kapan dibiarkan mengganggu seperti ini?", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Pemasangan Baligo Tidak Pada Tempatnya Saya kembali melihat ada baligo salah satu capres yang menempel di tembok bawah fly over laswi, sangat mengganggu pemandangan & kenyamanan", "category": "Satuan Polisi Pamong Praja Kota Bandung"},
    {"text": "Spanduk Partai Sangat menghalangi jalan trotoar di jl. ahmad yani kosambi sebrang ruko segitigamas kosambi kota bandung. sangat besar. tolong ya pak. trotoar minim jangan dipakai kampanye deh.", "category": "Satuan Polisi Pamong Praja Kota Bandung"},

]

# Convert text to lowercase for each entry in the dataset

def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def delete_links(input_text):
    pettern = r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''
    out_text = re.sub(pettern, ' ', input_text)
    return out_text

def delete_repeated_characters(input_text):
    pattern = r'(.)\1{2,}'
    out_text = re.sub(pattern, r"\1\1", input_text)
    return out_text

def clean_text(input_text):
    replace = r'[/(){}\[\]|@âÂ,;\?\'\"\*…؟–’،!&\+-:؛-]'
    out_text = re.sub(replace, " ", input_text)
    words = nltk.word_tokenize(out_text)
    words = [word for word in words if word.isalpha()]
    out_text = ' '.join(words)
    return out_text
# Remove punctuation for each entry in the dataset
for entry in data:
    entry["text"] = remove_punctuation(entry["text"].lower())
    entry["text"] = delete_links(entry["text"])
    entry["text"] = delete_repeated_characters(entry["text"])
    entry["text"] = clean_text(entry["text"])

# Print the modified dataset
for entry in data:
    print(entry["text"])

# Baca datasetf
dataset = pd.DataFrame(data)
dataset.to_csv("dataset_laporan_masyarakat.csv", index=False)

# Bagi dataset menjadi data pelatihan dan data pengujian
X_train, X_test, y_train, y_test = train_test_split(dataset['text'], dataset['category'], random_state=42)

# Buat model dengan pipeline
model = make_pipeline(TfidfVectorizer(stop_words=stopwords.words('indonesian'), tokenizer=PorterStemmer().stem), MultinomialNB())

# Latih model
model.fit(X_train, y_train)

# Prediksi kategori laporan pada data pengujian
predictions = model.predict(X_test)

# Evaluasi kinerja model
accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Akurasi: {accuracy}")

# Gunakan model untuk mengklasifikasikan laporan masyarakat baru
new_report = ["Blangko Ktp Habis Terus Ketika anak saya hendak membuat ktp dari tgl 27 jun 2023 sampai dgn sekarang diinfonya blangkonya kosong . padahal secara ketentuan max 2 minggu sudah selesai . apakah memang tidak tersedianya blangko? atkah kenapa ya? jalan lampu merah ".lower()]
predicted_category = model.predict(new_report)
print(f"Prediksi Kategori: {predicted_category}")


plt.plot(X_train,y_train)
plt.show()





#test data

#Dinas Sumber Daya Air dan Bina Marga Kota Bandung

#Mohon bantuan untuk dikeruk oleh dinas terkait , sebab akibat dari sampah pengerjaan trotoar di samping rumah jalan pasirkaliki no.140 / jalan dr.rum 1 kota bandung , kelurahan pasirkaliki kecamatan cicendo
#Hallo, berhubung jalan soekarno hatta (kiara condong- cibiru) trotoarnya baru diperbaiki dan rentan untuk dilalui pemotor yang tidak bertanggung jawab lebih baik dipasang bolard disetiap ujung dari trotoar, agar lebih terjaga dan tidak ada pkl yang berjualan. terima kasih



