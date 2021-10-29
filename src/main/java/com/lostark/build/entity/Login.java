package com.lostark.build.entity;

public class Login {
	
	private String id;
	private String pwd;
	
	public Login() {
		// TODO Auto-generated constructor stub
	}

	public Login(String id, String pwd) {
		super();
		this.id = id;
		this.pwd = pwd;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPwd() {
		return pwd;
	}

	public void setPwd(String pwd) {
		this.pwd = pwd;
	}

	@Override
	public String toString() {
		return "Login [id=" + id + ", pwd=" + pwd + ", getId()=" + getId() + ", getPwd()=" + getPwd() + ", getClass()="
				+ getClass() + ", hashCode()=" + hashCode() + ", toString()=" + super.toString() + "]";
	}
	
	

}
