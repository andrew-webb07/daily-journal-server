CREATE TABLE `Entry` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date`  TEXT NOT NULL,
    `concept`   TEXT NOT NULL,
    `journal_entry` TEXT NOT NULL,
    `mood_id`   INTEGER NOT NULL
);

CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY,
    `label` TEXT NOT NULL
);

CREATE TABLE `Tag` (
    `id` INTEGER NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);

CREATE TABLE `Entry_tag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id` INTEGER NOT NULL,
    `tag_id` INTEGER NOT NULL
);         

INSERT INTO `Mood` VALUES (null, "happy");
INSERT INTO `Mood` VALUES (null, "sad");
INSERT INTO `Mood` VALUES (null, "frustrated");
INSERT INTO `Mood` VALUES (null, "confused");
INSERT INTO `Mood` VALUES (null, "tired");
INSERT INTO `Mood` VALUES (null, "motivated");
INSERT INTO `Mood` VALUES (null, "ok");

INSERT INTO `Tag` VALUES (null, "API");
INSERT INTO `Tag` VALUES (null, "components");
INSERT INTO `Tag` VALUES (null, "fetch");

INSERT INTO `Entry` VALUES (null, "07/24/2025", "HTML & CSS", "We talked about HTML components and how to make grid layouts with Flexbox in CSS.", 7);
INSERT INTO `Entry` VALUES (null, "04/16/2021", "For Loops", "We went through objects and how to loop through them. We learned about key-value pairs and proper syntax for them. We also delved into using for loops in functions", 6);

INSERT INTO `Entry_tag` VALUES (null,1,2);
INSERT INTO `Entry_tag` VALUES (null,1,1);