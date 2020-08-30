# Database Challenge

## Deskripsi Sistem Secara Umum

DFD level 0 dibuat dengan asumsi bahwa Dashboard Analytic Admin (yang merupakan admin yang bertugas untuk melakukan campaign di Sosmed Instagram) dapat membuat post di instagram melalui Instageam Dashboard Analytic System yang dibuat. User yang akan melakukan posting dapat memasang sebuah tracker yang secara berkala mengambil data post like dan comment dari Instagram dalam rentang waktu tertentu. Setiap data yang masuk pada sistem adalah data like dan comment yang baru (bukan kumulatif).

Selain beberapa hal tersebut, pengguna juga dapat melakukan sentimen analysis. Sentimen analysis dilakukan dengan melakukan proses labelling terlebih dahulu. Proses labelling dilakukan dengan menggunakan data komentar yang telah dikumpulkan oleh cron job tracker dari sebuah posting. Setelah proses labelling selesai, maka proses training dilakukan. Proses training menggunakan algortime Naive Bayes dan karena training menggunakan Naive Bayes, maka data hasil training terdiri dari jumlah kata berdasarkan polaritas positif dan negatif. Karena data komentar bersifat unstructure maka perlu dilakukan proses MapReduce untuk mengubah data komentar menjadi data token kata.

Selain beberapa fitur diatas, fitur yang lain yaitu melihat data historis profile visit, data perkembangan follower dan data user demografi. Data ini dapat diakses dari data source NoSQL yang telah dibuat. Untuk mendapatkan data demografi user, perlu ada koneksi dulu ke API Instagram untuk mendapatkan data geo-location dari user.

## Deskripsi File pada direktori database-challenge

- `problem-description.md`: Text file yang berisi soal dari Database Challenge
- `README.md`: File Ini
- `DFD`: File Data Flow Diagram (DFD). Format yang digunakan adalah .drawio dan dapat dilihat melalui tautan berikut [https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FDFD](https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FDFD)
- `ERD.drawio`: File Entity Relationship Diagram (ERD) yang merupakan diagram untuk database SQL. Format yang digunakan adalah .drawio dan dapat dilihat melalui tautan berikut [https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FERD.drawio](https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FERD.drawio)
- `NoSQL data structure.drawio`: File diagram untuk struktur data pada database NoSQL. Format yang digunakan adalah .drawio dan dapat dilihat melalui tautan berikut [https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FNoSQL%20data%20structure.drawio](https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FNoSQL%20data%20structure.drawio)
- `Cron Data Pipeline Architecture`: File diagram yang berisi penjelasan sederhana terkait arsitektur cron job/scheduler yang akan digunakan. Format yang digunakan adalah .drawio dan dapat dilihat melalui tautan berikut [https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FCron%20Data%20Pipeline%20Architecture](https://app.diagrams.net/#Hdesenfirman%2Flautan-natural-krimerindo%2Fmaster%2Fdatabase-challenge%2FCron%20Data%20Pipeline%20Architecture)
