DROP DATABASE IF EXISTS swiftsynk;
CREATE DATABASE swiftsynk;
USE swiftsynk;
CREATE TABLE user(
				email varchar(50) primary key not null,
                password varchar(12),
                username varchar(45),
                base_folder_id varchar(50)
);

Create table folder (
					folder_id varchar(50) primary key,
                    folder_path varchar(250),
                    email varchar (50),
                    foreign key (Email) references User(email)
);

Create table file (
					file_id varchar(55) primary key,
                    status varchar(100),
                    filepath varchar(250),
                    upload_time varchar(25),
                    folder_id varchar(50),
                    foreign key (folder_id) references folder(folder_id)
);

DELIMITER SS
CREATE TRIGGER addBaseFolder
	AFTER INSERT
    ON user FOR EACH ROW
    BEGIN
		INSERT INTO folder VALUES(NEW.base_folder_id, "BASE", NEW.email);
	END
SS
DELIMITER ;

insert into user values("narendradukhande30@gmail.com","hii","Narendra", "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n");
-- insert into user values("varadesanchita@gmail.com","sanchi@11","Sanchita", "efgh");
-- insert into user values("saiff@gmail.com","saif@16","Saifuddin", "jklm");
-- insert into folder values("1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n", "BASE","narendradukhande30@gmail.com");
-- insert into folder values("efgh", "some\\path","varadesanchita@gmail.com");
-- insert into folder values("jklm", "some\\path","saiff@gmail.com");
-- insert into file values("1dM3brV3OM80SM6L4mhHifbxuzGCuoVdM","Modified","C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt","24/02/23 16:40:01","1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n");
-- insert into file values("uvw","Modified","c:folder/py","16:06","efgh");
-- insert into file values("pqr","Sync","c:files/java","16:09","jklm");

