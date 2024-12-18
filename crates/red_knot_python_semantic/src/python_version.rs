use std::fmt;

/// Representation of a Python version.
///
/// Unlike the `TargetVersion` enums in the CLI crates,
/// this does not necessarily represent a Python version that we actually support.
#[derive(Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct PythonVersion {
    pub major: u8,
    pub minor: u8,
}

impl PythonVersion {
    pub const PY37: PythonVersion = PythonVersion { major: 3, minor: 7 };
    pub const PY38: PythonVersion = PythonVersion { major: 3, minor: 8 };
    pub const PY39: PythonVersion = PythonVersion { major: 3, minor: 9 };
    pub const PY310: PythonVersion = PythonVersion {
        major: 3,
        minor: 10,
    };
    pub const PY311: PythonVersion = PythonVersion {
        major: 3,
        minor: 11,
    };
    pub const PY312: PythonVersion = PythonVersion {
        major: 3,
        minor: 12,
    };
    pub const PY313: PythonVersion = PythonVersion {
        major: 3,
        minor: 13,
    };

    pub fn free_threaded_build_available(self) -> bool {
        self >= PythonVersion::PY313
    }
}

impl Default for PythonVersion {
    fn default() -> Self {
        Self::PY39
    }
}

impl TryFrom<(&str, &str)> for PythonVersion {
    type Error = std::num::ParseIntError;

    fn try_from(value: (&str, &str)) -> Result<Self, Self::Error> {
        let (major, minor) = value;
        Ok(Self {
            major: major.parse()?,
            minor: minor.parse()?,
        })
    }
}

impl From<(u8, u8)> for PythonVersion {
    fn from(value: (u8, u8)) -> Self {
        let (major, minor) = value;
        Self { major, minor }
    }
}

impl fmt::Display for PythonVersion {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let PythonVersion { major, minor } = self;
        write!(f, "{major}.{minor}")
    }
}

#[cfg(feature = "serde")]
impl<'de> serde::Deserialize<'de> for PythonVersion {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        let as_str = String::deserialize(deserializer)?;

        if let Some((major, minor)) = as_str.split_once('.') {
            let major = major
                .parse()
                .map_err(|err| serde::de::Error::custom(format!("invalid major version: {err}")))?;
            let minor = minor
                .parse()
                .map_err(|err| serde::de::Error::custom(format!("invalid minor version: {err}")))?;

            Ok((major, minor).into())
        } else {
            let major = as_str.parse().map_err(|err| {
                serde::de::Error::custom(format!(
                    "invalid python-version: {err}, expected: `major.minor`"
                ))
            })?;

            Ok((major, 0).into())
        }
    }
}

#[cfg(feature = "serde")]
impl serde::Serialize for PythonVersion {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        serializer.serialize_str(&self.to_string())
    }
}
