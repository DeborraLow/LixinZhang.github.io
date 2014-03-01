Title: JDBC 简单数据库操作
Date: 2011-06-05 13:02
Author: 糖拌咸鱼
Slug: jdbc-jian-dan-shu-ju-ku-cao-zuo

<div class="cnblogs_code">

</p>
<p>
     1 package cose.seu.edu.cn.cosersoft; 2 import java.sql.*; 3 public class Test { 4     /* 5      * Create a connection to MYSQL database 6      */ 7     public static Connection getConnection()  8         throws ClassNotFoundException, SQLException{ 9         String url="jdbc:mysql://127.0.0.1:3306/myDb";10         Class.forName("com.mysql.jdbc.Driver");11         String username="root";12         String password="coser";13         Connection conn = DriverManager.getConnection(url, username, password);14         return conn;15     }16     public static void PrintResult(ResultSet rs) throws SQLException{17         while(rs.next()){18             System.out.println(rs.getInt(1));19         }20     }21     public static void main(String [] args) throws Exception{22         Connection conn = getConnection();23         Statement sqlstate = conn.createStatement();24         if(!conn.isClosed())25             System.out.println("连接数据库成功");26         else System.out.println("连接数据库失败");        27         //Execute common sql text;28         String sqltext = "select * from mytb";29         ResultSet rs = sqlstate.executeQuery(sqltext);30         PrintResult(rs);31         sqlstate.close();32         //Call procedure with no parameters33         CallableStatement cs = conn.prepareCall("{call myPro()}");34         rs=cs.executeQuery();35         PrintResult(rs);36         cs.close();37         //Call procedure with parameters38         CallableStatement cs2 = conn.prepareCall("{call pr_Add(?)}");39         //add parameter40         cs2.setInt(1, 1001);41         cs2.execute();42         System.out.println("Insert successfully!");43         cs2.close();44         conn.close();45     }46 }

</p>
<p>

</div>

</p>

