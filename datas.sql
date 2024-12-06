/*
 Navicat Premium Dump SQL

 Source Server         : class01
 Source Server Type    : MySQL
 Source Server Version : 80039 (8.0.39)
 Source Host           : localhost:3306
 Source Schema         : datas

 Target Server Type    : MySQL
 Target Server Version : 80039 (8.0.39)
 File Encoding         : 65001

 Date: 06/12/2024 21:46:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classinfo
-- ----------------------------
DROP TABLE IF EXISTS `classinfo`;
CREATE TABLE `classinfo`  (
  `class_id` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cls_rank` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `head_teacher` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `student_count` int NOT NULL,
  PRIMARY KEY (`class_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '班级信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classinfo
-- ----------------------------
INSERT INTO `classinfo` VALUES ('ClassA', '1', 'TeacherA', 10);
INSERT INTO `classinfo` VALUES ('ClassB', '2', 'TeacherB', 10);
INSERT INTO `classinfo` VALUES ('ClassC', '3', 'TeacherC', 10);

-- ----------------------------
-- Table structure for studentenrollment
-- ----------------------------
DROP TABLE IF EXISTS `studentenrollment`;
CREATE TABLE `studentenrollment`  (
  `student_id` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stu_name` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `class_` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `birth_date` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `school` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`student_id`) USING BTREE,
  INDEX `fk_class`(`class_` ASC) USING BTREE,
  CONSTRAINT `fk_class` FOREIGN KEY (`class_`) REFERENCES `classinfo` (`class_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '学生学籍信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentenrollment
-- ----------------------------
INSERT INTO `studentenrollment` VALUES ('A01', 'wjh', '男', 'classA', '2003-11-26', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A02', 'wjh', 'male', 'classa', '2002-6-6', '是更好的士大夫嘎嘎');
INSERT INTO `studentenrollment` VALUES ('A03', 'Charlie', 'Male', 'ClassA', '2002-03-03', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A04', 'Diana', 'Female', 'ClassA', '2002-04-04', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A05', 'Ethan', 'Male', 'ClassA', '2002-05-05', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A06', 'Fiona', 'Female', 'ClassA', '2002-06-06', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A07', 'George', 'Male', 'ClassA', '2002-07-07', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A08', 'Hannah', 'Female', 'ClassA', '2002-08-08', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A09', 'Ivan', 'Male', 'ClassA', '2002-09-09', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('A10', 'Julia', 'Female', 'ClassA', '2002-10-10', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B01', '赵天宇', '男', 'ClassB', '2003-01-01', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B02', '钱晓晓', '女', 'ClassB', '2003-02-02', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B03', '孙丽丽', '女', 'ClassB', '2003-03-03', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B04', '李强', '男', 'ClassB', '2003-04-04', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B05', '周梅', '女', 'ClassB', '2003-05-05', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B06', '吴刚', '男', 'ClassB', '2003-06-06', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B07', '郑洁', '女', 'ClassB', '2003-07-07', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B08', '王磊', '男', 'ClassB', '2003-08-08', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B09', '陈静', '女', 'ClassB', '2003-09-09', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('B10', '郭阳', '男', 'ClassB', '2003-10-10', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C01', '萧炎', '男', 'ClassC', '2004-01-01', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C02', '云韵', '女', 'ClassC', '2004-02-02', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C03', '美杜莎', '女', 'ClassC', '2004-03-03', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C04', '药老', '男', 'ClassC', '2004-04-04', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C05', '小医仙', '女', 'ClassC', '2004-05-05', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C06', '萧薰儿', '女', 'ClassC', '2004-06-06', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C07', '纳兰嫣然', '女', 'ClassC', '2004-07-07', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C08', '海波东', '男', 'ClassC', '2004-08-08', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C09', '紫妍', '女', 'ClassC', '2004-09-09', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('C10', '林修崖', '男', 'ClassC', '2004-10-10', '海南师范大学');
INSERT INTO `studentenrollment` VALUES ('string', 'string', 'string', 'ClassA', 'string', 'string');

-- ----------------------------
-- Table structure for studentscores
-- ----------------------------
DROP TABLE IF EXISTS `studentscores`;
CREATE TABLE `studentscores`  (
  `student_id` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stu_name` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `total_score` int NOT NULL,
  `score_rank` int NOT NULL,
  `class_` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`student_id`) USING BTREE,
  CONSTRAINT `fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `studentenrollment` (`student_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '学生成绩信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentscores
-- ----------------------------
INSERT INTO `studentscores` VALUES ('A01', 'wjh', 999, 1, 'ClassA');
INSERT INTO `studentscores` VALUES ('A03', 'Charlie', 88, 3, 'ClassA');
INSERT INTO `studentscores` VALUES ('A04', 'Diana', 92, 4, 'ClassA');
INSERT INTO `studentscores` VALUES ('A05', 'Ethan', 82, 5, 'ClassA');
INSERT INTO `studentscores` VALUES ('A06', 'Fiona', 87, 6, 'ClassA');
INSERT INTO `studentscores` VALUES ('A07', 'George', 91, 7, 'ClassA');
INSERT INTO `studentscores` VALUES ('A08', 'Hannah', 84, 8, 'ClassA');
INSERT INTO `studentscores` VALUES ('A09', 'Ivan', 89, 9, 'ClassA');
INSERT INTO `studentscores` VALUES ('A10', 'Julia', 86, 10, 'ClassA');
INSERT INTO `studentscores` VALUES ('B01', '赵天宇', 85, 1, 'ClassB');
INSERT INTO `studentscores` VALUES ('B02', '钱晓晓', 88, 2, 'ClassB');
INSERT INTO `studentscores` VALUES ('B03', '孙丽丽', 82, 3, 'ClassB');
INSERT INTO `studentscores` VALUES ('B04', '李强', 90, 4, 'ClassB');
INSERT INTO `studentscores` VALUES ('B05', '周梅', 87, 5, 'ClassB');
INSERT INTO `studentscores` VALUES ('B06', '吴刚', 84, 6, 'ClassB');
INSERT INTO `studentscores` VALUES ('B07', '郑洁', 89, 7, 'ClassB');
INSERT INTO `studentscores` VALUES ('B08', '王磊', 86, 8, 'ClassB');
INSERT INTO `studentscores` VALUES ('B09', '陈静', 83, 9, 'ClassB');
INSERT INTO `studentscores` VALUES ('B10', '郭阳', 80, 10, 'ClassB');
INSERT INTO `studentscores` VALUES ('C01', '萧炎', 92, 1, 'ClassC');
INSERT INTO `studentscores` VALUES ('C02', '云韵', 88, 2, 'ClassC');
INSERT INTO `studentscores` VALUES ('C03', '美杜莎', 90, 3, 'ClassC');
INSERT INTO `studentscores` VALUES ('C04', '药老', 87, 4, 'ClassC');
INSERT INTO `studentscores` VALUES ('C05', '小医仙', 85, 5, 'ClassC');
INSERT INTO `studentscores` VALUES ('C06', '萧薰儿', 91, 6, 'ClassC');
INSERT INTO `studentscores` VALUES ('C07', '纳兰嫣然', 89, 7, 'ClassC');
INSERT INTO `studentscores` VALUES ('C08', '海波东', 86, 8, 'ClassC');
INSERT INTO `studentscores` VALUES ('C09', '紫妍', 84, 9, 'ClassC');
INSERT INTO `studentscores` VALUES ('C10', '林修崖', 83, 10, 'ClassC');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `registration_date` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `is_admin` tinyint(1) NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'wjh', '111111', '2024-11-30 16:55:32', 0);
INSERT INTO `users` VALUES (2, 'admin', '123456', '2024-12-02 13:16:37', 1);
INSERT INTO `users` VALUES (3, 'string', 'string', '2024-12-05 20:08:05', 0);
INSERT INTO `users` VALUES (4, 'w', '000000', '2024-12-05 23:33:42', 0);
INSERT INTO `users` VALUES (5, 'mjt', '000000', '2024-12-06 18:54:22', 0);

-- ----------------------------
-- View structure for studentscoreswithtotalrank
-- ----------------------------
DROP VIEW IF EXISTS `studentscoreswithtotalrank`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `studentscoreswithtotalrank` AS select `studentscores`.`student_id` AS `student_id`,`studentscores`.`stu_name` AS `stu_name`,`studentscores`.`total_score` AS `total_score`,rank() OVER (ORDER BY `studentscores`.`total_score` desc )  AS `score_rank`,`studentscores`.`class_` AS `class_` from `studentscores`;

-- ----------------------------
-- View structure for viewclassinfo
-- ----------------------------
DROP VIEW IF EXISTS `viewclassinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `viewclassinfo` AS select `ci`.`class_id` AS `class_id`,`ci`.`cls_rank` AS `cls_rank`,`ci`.`head_teacher` AS `head_teacher`,count(`se`.`class_`) AS `student_count` from (`classinfo` `ci` left join `studentenrollment` `se` on((`ci`.`class_id` = `se`.`class_`))) group by `ci`.`class_id`,`ci`.`cls_rank`,`ci`.`head_teacher`;

-- ----------------------------
-- View structure for viewstudentenrollment
-- ----------------------------
DROP VIEW IF EXISTS `viewstudentenrollment`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `viewstudentenrollment` AS select `studentenrollment`.`student_id` AS `student_id`,`studentenrollment`.`stu_name` AS `stu_name`,`studentenrollment`.`gender` AS `gender`,`studentenrollment`.`class_` AS `class_`,`studentenrollment`.`birth_date` AS `birth_date`,`studentenrollment`.`school` AS `school` from `studentenrollment`;

SET FOREIGN_KEY_CHECKS = 1;
