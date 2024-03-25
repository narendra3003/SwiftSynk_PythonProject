DROP DATABASE IF EXISTS swiftsynk;
CREATE DATABASE swiftsynk;
USE swiftsynk;
CREATE TABLE user(
	email varchar(50) primary key not null,
    password varchar(12),
    username varchar(45),
    base_folder_id varchar(50),
    secondary_folder_id varchar(50)
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
    filepath varchar(250) unique,
    upload_time varchar(25),
    folder_id varchar(50),
    foreign key (folder_id) references folder(folder_id)
);

Create table lastVersions (
	last_version_id varchar(55) primary key,
    main_file_id varchar(55),
  foreign key (main_file_id) references file(file_id)
);

DELIMITER SS
CREATE TRIGGER addBaseFolder
	AFTER INSERT
    ON user FOR EACH ROW
    BEGIN
		INSERT INTO folder VALUES(NEW.base_folder_id, "BASE", NEW.email);
        INSERT INTO folder VALUES(NEW.secondary_folder_id, "SECOND", NEW.email);
	END
SS
DELIMITER ;


create table logtable(
    Tablename varchar (20),
    activity varchar (20),
    descript varchar (100),
    Time_stamp datetime
);


DELIMITER SS
CREATE TRIGGER insertFile
	AFTER INSERT
    ON file FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("File", "insert",new.file_id, now());
	END
SS
DELIMITER ;

DELIMITER SS
CREATE TRIGGER insertUser
	AFTER INSERT
    ON user FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("User","insert",new.email, now());
	END
SS
DELIMITER ;

DELIMITER SS
CREATE TRIGGER insertFolder
	AFTER INSERT
    ON folder FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("Folder", "insert", new.folder_id, now());
	END
SS
DELIMITER ;


DELIMITER SS
CREATE TRIGGER UpdateFolder
	AFTER UPDATE
    ON folder FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("Folder", "update", new.folder_id, now());
	END
SS
DELIMITER ;

DELIMITER SS
CREATE TRIGGER UpdateUser
	AFTER UPDATE
    ON user FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("Folder", "update", new.email, now());
	END
SS
DELIMITER ;

DELIMITER SS
CREATE TRIGGER UpdateFile
	AFTER UPDATE
    ON file FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("File", "update", new.file_id, now());
	END
SS
DELIMITER ;


DELIMITER SS
CREATE TRIGGER DeleteFolder
	before DELETE
    ON folder FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("Folder", "delete", old.folder_id, now());
	END
SS
DELIMITER ;

DELIMITER SS
CREATE TRIGGER DeleteUser
	before DELETE
    ON user FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("Folder", "delete", old.email, now());
	END
SS
DELIMITER ;

DELIMITER SS
CREATE TRIGGER DeleteFile
	before DELETE
    ON file FOR EACH ROW
    BEGIN
		INSERT INTO logtable VALUES("File", "delete", old.file_id, now());
	END
SS
DELIMITER ;

-- insert into user values("syedsaif78676@gmail.com","hii","Saif", "1rEgaGA5mofkeCf572WVRkOWIj_4sHaWm");
-- insert into user values("varadesanchita@gmail.com","sanchi","Sanchita", "12QDJynTGSmbyv4Jf6w8ZYzH-NwgYOSt8");
insert into user values("narendradukhande30@gmail.com","hii","Narendra", "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n", "16OGxSt74hhmluHekVRs6RRfvoJ1XZdxS");
-- insert into user values("saiff@gmail.com","saif@16","Saifuddin", "jklm");
-- insert into folder values("1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n", "BASE","narendradukhande30@gmail.com");
-- insert into folder values("efgh", "some\\path","varadesanchita@gmail.com");
-- insert into folder values("jklm", "some\\path","saiff@gmail.com");
-- insert into file values("1dM3brV3OM80SM6L4mhHifbxuzGCuoVdM","Modified","C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt","24/02/23 16:40:01","1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n");
-- insert into file values("uvw","Modified","c:folder/py","16:06","efgh");
-- insert into file values("pqr","Sync","c:files/java","16:09","jklm");

-- insert into logtable values ("File", "modified","0.0026 sec")


