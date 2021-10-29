package com.lostark.build.dao;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import com.lostark.build.entity.Login;

@Mapper
public interface LoginDao {

	@Select("select * from admin")
	List<Login> getList();

}
