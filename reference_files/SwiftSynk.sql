drop database swiftsynK;
Create database SwiftSynk;
use SwiftSynk;
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
                    filepath varchar(250),LastModifiedTime varchar(25),Filesize varchar (20),
                    foreign key (folder_id) references folder(folder_id)
                
);

use SwiftSynk;

insert into User values("narendra@gmail.com","tejas@30","Narendra");
insert into User values("varadesanchita@gmail.com","sanchi@11","Sanchita");
insert into User values("saiff@gmail.com","saif@16","Saifuddin");
insert into folder values("abcd","narendra@gmail.com");
insert into folder values("efgh","varadesanchita@gmail.com");
insert into folder values("jklm","saiff@gmail.com");
insert into file values("xyz","Modified","abcd","c:files/cp","16:01","245kb");
insert into file values("uvw","Modified","efgh","c:folder/py","16:06","650kb");
insert into file values("pqr","Sync","jklm","c:files/java","16:09","565kb");



