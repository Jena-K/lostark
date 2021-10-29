package com.lostark.build.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.lostark.build.dao.LoginDao;
import com.lostark.build.entity.Login;

@Service
public class LoginServiceImp implements LoginService{

	@Autowired
	private LoginDao loginDao;
	
	@Override
	public List<Login> getList() {
	
		List<Login> list = loginDao.getList();
		
		return list;
	}

}
