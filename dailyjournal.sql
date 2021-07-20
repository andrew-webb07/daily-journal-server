CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` TEXT NOT NULL,
    `address` TEXT NOT NULL,
    `moodId` INTEGER NOT NULL
);

CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY
    `label` TEXT NOT NULL
);



INSERT INTO `Mood` VALUES (null, "happy");
INSERT INTO `Mood` VALUES (null, "sad");
INSERT INTO `Mood` VALUES (null, "frustrated");
INSERT INTO `Mood` VALUES (null, "confused");
INSERT INTO `Mood` VALUES (null, "tired");
INSERT INTO `Mood` VALUES (null, "motivated");
INSERT INTO `Mood` VALUES (null, "ok");

INSERT INTO `Entry` VALUES (null, "07/24/2025", "HTML & CSS", "We talked about HTML components and how to make grid layouts with Flexbox in CSS.", 7);
INSERT INTO `Entry` VALUES (null, "04/16/2021", "For Loops", "We went through objects and how to loop through them. We learned about key-value pairs and proper syntax for them. We also delved into using for loops in functions", 6);