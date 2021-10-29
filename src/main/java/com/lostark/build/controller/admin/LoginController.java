package com.lostark.build.controller.admin;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.lostark.build.entity.Login;
import com.lostark.build.service.LoginService;

@Controller
@RequestMapping("/admin/")
public class LoginController {

	@Autowired
	private LoginService service;
	
	@RequestMapping("login")
	public String form() {
		
		return "admin/login/form";
	}
	
	@RequestMapping("auth")
	public String auth() {
	
		return "admin/login/auth";
	}
	
	@RequestMapping("welcome")
	public String welcome() {
		
		return "admin/login/welcome";
	}
}
