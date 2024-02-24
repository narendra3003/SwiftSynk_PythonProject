DROP DATABASE IF EXISTS swiftsynk;
CREATE DATABASE swiftsynk;
USE swiftsynk;
CREATE TABLE User(
				Email varchar(50) primary key not null,
                password varchar(12), Username varchar(45)
);

Create table folder (
					folder_id varchar(50) primary key,Email varchar (50),
                    foreign key (Email) references User(Email)
);

Create table file (
					file_id varchar(55) primary key,Status varchar(100),folder_id varchar(50),
                    filepath varchar(250),upload varchar(25),
                    foreign key (folder_id) references folder(folder_id)
                
);

use SwiftSynk;

insert into User values("narendradukhande30@gmail.com","tejas@30","Narendra");
insert into User values("varadesanchita@gmail.com","sanchi@11","Sanchita");
insert into User values("saiff@gmail.com","saif@16","Saifuddin");
insert into folder values("1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n","narendradukhande30@gmail.com");
insert into folder values("efgh","varadesanchita@gmail.com");
insert into folder values("jklm","saiff@gmail.com");
insert into file values("1dM3brV3OM80SM6L4mhHifbxuzGCuoVdM","Modified","1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n","C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files\\test.txt","24/02/23 16:40:01");
insert into file values("uvw","Modified","efgh","c:folder/py","16:06");
insert into file values("pqr","Sync","jklm","c:files/java","16:09");

