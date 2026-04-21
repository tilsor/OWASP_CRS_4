Summary: ModSecurity Rules
Name: mod_security_crs
Version: 4.25.0
Release: 0%{?dist}
License: ASL 2.0
URL: https://coreruleset.org
Group: System Environment/Daemons
#Source: https://github.com/coreruleset/coreruleset/archive/refs/tags/v%{version}.tar.gz
Source: https://github.com/coreruleset/coreruleset/releases/download/v4.25.0/coreruleset-%{version}-minimal.tar.gz
BuildArch: noarch
Requires: mod_security >= 2.9.6
Obsoletes: mod_security_crs-extras < 3.0.0

%description
This package provides the base rules for mod_security.

%prep
%setup -q -n coreruleset-%{version}

%build

%install

install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules
install -d %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules

# To exclude rules (pre/post)
mv rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
mv rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf

install -m0644 rules/* %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/
mv crs-setup.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf

# activate base_rules
for f in `ls %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/` ; do
    ln -s %{_datarootdir}/mod_modsecurity_crs/rules/$f %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f;
done

%files
%license LICENSE
#%doc SECURITY.md SPONSORS.md CHANGES.md README.md
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/activated_rules/*
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf
%{_datarootdir}/mod_modsecurity_crs


%changelog
* Tue Apr 21 2026 German Gonzalez <ggonzalez@tilsor.com.uy> - 4.25.0
- Generate RPM for CRS v4.25.0 LTS  
