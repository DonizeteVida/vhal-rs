use pest::Parser;
use pest_derive::Parser;

#[derive(Parser)]
#[grammar = "sintax/apx.pest"]
pub struct ApxParser;

pub fn from_lib() {
    println!("calling a lib function")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn should_parse_a_single_header() {
        let input =
        r#"APX/1.2
        "#;

        let pairs = ApxParser::parse(Rule::document, input).expect("parse error");
        assert_eq!(1, pairs.len());
    }
}
