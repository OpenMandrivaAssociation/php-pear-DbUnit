%define  upstream_name DbUnit

Summary:	DbUnit port for PHP/PHPUnit to support database interaction testing
Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	4
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/DbUnit-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-symfony-YAML >= 1.0.2

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides DbUnit port for PHP/PHPUnit to support database
interaction testing.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/ChangeLog.markdown
%doc %{upstream_name}-%{version}/LICENSE
%{_bindir}/dbunit
%{_datadir}/pear/PHPUnit/Extensions/Database
%{_datadir}/pear/packages/DbUnit.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2012.0
+ Revision: 741934
- fix major breakage by careless packager

* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1
+ Revision: 730865
- import php-pear-DbUnit


* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2010.2
- initial Mandriva package
